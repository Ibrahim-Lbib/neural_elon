# wrappers for API calls
import openai
from dotenv import load_dotenv
import os

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

def generate_ideas(topic: str, num_ideas: int = 5, creativity: int = 7) -> list:
    client = openai.OpenAI(
        api_key=os.getenv("NEURAL_ELON_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )
    
    prompt = (
        f"Generate {num_ideas} bold startup ideas about {topic}.\n"
        f"Creativity level: {creativity}/10 (1=safe, 10=insane but brilliant).\n"
        "Return only a numbered list. Example:\n"
        "1. Solar-powered underground cities\n"
        "2. AI that turn trash into rockets"
    )
    
    response = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct:free",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=600,
        temperature=0.7 + (creativity * 0.1)
    )
    
    raw_text = response.choices[0].message.content
    lines = [line.strip() for line in raw_text.split("\n") if line.strip()]
    ideas = []
    for line in lines:
        if any(line.startswith(f"{i}.") for i in range(1, 21)) or any(line.startswith(f"{i}") for i in range(1, 21)):
            idea = line.split(".", 1)[-1].split(")", 1)[-1].strip()
            ideas.append(idea)
    return ideas if ideas else lines[:num_ideas]

if __name__ == "__main__":
    check_api_key()
    print("\n" + "="*50)
    print("NEURAL ELON IS THINKING...")
    print("="*50)

    ideas = generate_ideas("artificial intelligence", 6, 8)
    for i, idea in enumerate(ideas, 1):
        print(f"{i}. {idea}") 