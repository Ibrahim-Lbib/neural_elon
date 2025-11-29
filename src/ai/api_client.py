# wrappers for API calls
import openai
from dotenv import load_dotenv
import os
from src.ai.prompt_builder import build_idea_prompt
import re

load_dotenv()  # Load environment variables from .env file

def check_api_key():
    api_key = os.getenv("NEURAL_ELON_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set NEURAL_ELON_API_KEY in your environment variables.")
    
    # Set my key (use env var for security)
    client = openai.OpenAI(
        api_key=api_key,  # Or hardcode for testing: "sk-your-key-here"
        base_url="https://openrouter.ai/api/v1"
    )

    response = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct:free",  # A free model
        messages=[{"role": "user", "content": "Say exactly these three words: Hello Neural Elon"}],
        max_tokens=10
    )

    print("Success! The AI replied")
    print(response.choices[0].message.content)
    return response

def generate_ideas(topic, num_ideas, creativity) -> list:
    client = openai.OpenAI(
        api_key=os.getenv("NEURAL_ELON_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )
    
    prompt = f"""
You are Elon Musk brainstorming insane startup ideas.
Generate EXACTLY {num_ideas} startup ideas about: {topic}
Creativity: {creativity}/10
Rules:
- ONE idea per line
- Start with number and period: 1. 2. 3. etc.
- Maximum 18 words per idea
- No intro, no outro, no explanations
- ONLY the numbered list

Example:
1. AI tutor that learns from your dreams
2. School on Mars with zero-gravity exams
3. Neuralink group chat for study groups
    """
    
    response = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct:free",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=0.8 + (creativity * 0.1)
    )
    
    raw = response.choices[0].message.content.strip()
    ideas = []
    for line in raw.split("\n"):
        line = line.strip()
        if not line:
            continue
        
        if re.match(r'^\d+\.\s', line):
            idea = line.split('.', 1)[1].strip()
            if idea and len(idea) > 10:
                ideas.append(idea)
        
    if len(ideas) < num_ideas:
        lines = [line.strip() for l in raw.split("\n") if l.strip() and len(l.strip()) > 15]
        for line in lines:
            clean = re.sub(r'^\d+[\.\)\s\-\•\*]\s*', '', line).strip()
            if clean and clean not in ideas:
                ideas.append(clean)
            
    if not ideas:
        ideas = [f"[Ideea {i+1}: Model returned weird format — try again]"]
        
    return ideas[:num_ideas]
        
if __name__ == "__main__":
    check_api_key()
    print("\n" + "="*50)
    print("NEURAL ELON IS THINKING...")
    print("="*50)

    topic = input("Enter a topic for startup ideas: ")
    num_ideas = int(input("How many ideas to generate? "))
    creativity = int(input("Creativity level (1-10)? "))
    ideas = generate_ideas(topic, num_ideas, creativity)
    for i, idea in enumerate(ideas, 1):
        print(f"{i}. {idea}") 