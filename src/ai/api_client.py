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
    
    # Set your key (use env var for security)
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
    
    prompt = build_idea_prompt(topic, num_ideas, creativity)
    
    response = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct:free",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=0.8 + (creativity * 0.1)
    )
    
    raw = response.choices[0].message.content.strip()
    print("Raw AI response:\n", raw)  # ← Remove this later, great for debugging now!
    
    ideas = []
    lines = raw.split("\n")
    
    for line in lines:
        line = line.strip()
        if not line or len(line) < 10:
            continue
            
        # Remove common prefixes: 1. 1) 1- 1: • - * »
        clean = re.sub(r'^[\d\)\]\-\•\*\>\:]+\s*[\.\)\]\-\•\*\>\:]*\s*', '', line, count=1)
        clean = clean.strip('"\'-•* []')
        
        if clean and 10 < len(clean) < 200 and clean not in ideas:
            ideas.append(clean)
    
    # Fallback: split by any numbered/bulleted pattern
    if len(ideas) < num_ideas:
        fallback = re.findall(r'(?:\d+[\.\)\]\-\:]\s*|[\•\-\*]\s*)([^\\n]{15,120})', raw)
        for match in fallback:
            clean = match.strip('"\'-•* ')
            if clean and clean not in ideas:
                ideas.append(clean)
    
    # Final desperate fallback
    if not ideas:
        ideas = [f"Raw idea {i+1}: {line}" for i, line in enumerate(lines[:num_ideas]) if line.strip()]
    
    return ideas[:num_ideas]
