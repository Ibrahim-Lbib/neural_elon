# wrappers for API calls
import openai
from dotenv import load_dotenv
import os
from src.ai.prompt_builder import build_idea_prompt
import re
from colorama import Fore, init

init(autoreset=True)  # Initialize colorama
load_dotenv()  # Load environment variables from .env file

def check_api_key():
    api_key = os.getenv("NEURAL_ELON_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set NEURAL_ELON_API_KEY in your environment variables.")
    
    models_to_test = [
        "meta-llama/llama-3.3-70b-instruct:free",   # your current one
        "mistralai/mistral-7b-instruct:free",       # usually works
        "qwen/qwen-2-72b-instruct:free",            # solid backup
        "google/gemini-flash-1.5-exp",  
        "arcee-ai/trinity-mini:free",
        "tngtech/tng-r1t-chimera:free",
        "allenai/olmo-3-32b-think:free",
        "kwaipilot/kat-coder-pro:free",
        "nvidia/nemotron-nano-12b-v2-vl:free",
        "amazon/nova-2-lite-v1:free"
    ]
    for model in models_to_test:
        try:
                    
            # Set your key (use env var for security)
            client = openai.OpenAI(
                api_key=api_key,  # Or hardcode for testing: "sk-your-key-here"
                base_url="https://openrouter.ai/api/v1"
            )

            response = client.chat.completions.create(
                model=model,  # A free model
                messages=[{"role": "user", "content": "Say exactly these three words: Hello Neural Elon"}],
                max_tokens=1000
            )

            print("Success! The AI replied")
            print(response.choices[0].message.content)
            return response
        except:
            continue
        
    raise ConnectionError("All test models failed. Please check your API key and network connection.")

def generate_ideas(topic, num_ideas, creativity) -> list:
    # === LIST OF FALLBACK MODELS (free + reliable) ===
    FALLBACK_MODELS = [
        "meta-llama/llama-3.3-70b-instruct:free",   # your current one
        "mistralai/mistral-7b-instruct:free",       # usually works
        "qwen/qwen-2-72b-instruct:free",            # solid backup
        "google/gemini-flash-1.5-exp",  
        "arcee-ai/trinity-mini:free",
        "tngtech/tng-r1t-chimera:free",
        "allenai/olmo-3-32b-think:free",
        "kwaipilot/kat-coder-pro:free",
        "nvidia/nemotron-nano-12b-v2-vl:free",
        "amazon/nova-2-lite-v1:free"
    ]
    
    prompt = build_idea_prompt(topic, num_ideas, creativity)
    
    for model in FALLBACK_MODELS:
        # Friendly message
        friendly_name = model.split("/")[-1].split(":")[0]
        print(Fore.YELLOW + f"Trying {friendly_name}...")
        
        try:
            client = openai.OpenAI(
                api_key=os.getenv("NEURAL_ELON_API_KEY"),
                base_url="https://openrouter.ai/api/v1"
            )
                
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=2000,
                temperature=0.8 + (creativity * 0.1)
            )
            
            raw = response.choices[0].message.content.strip()
            # print("Raw AI response:\n", raw)  # ← Remove this later, great for debugging now!
            
            ideas = []
            lines = raw.split("\n")
            
            for line in lines:
                line = line.strip()
                if not line or len(line) < 10:
                    continue
                    
                # Remove common prefixes: 1. 1) 1- 1: • - * »
                clean = re.sub(r'^\s*[\d\)\]\-\•\*\>\:]+[\.\)\]\-\•\*\>\:]*\s*', '', line, count=1)
                clean = clean.strip(' "\'-•*[]()')
                
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
                
            ideas = [re.sub(r'\*\*(.*?)\*\*', r'\1', idea) for idea in ideas]  # remove **bold**
            ideas = [re.sub(r'[_*`]', '', idea) for idea in ideas]  # remove leftover markdown
            
            return ideas[:num_ideas]
        except Exception as e:
            print(Fore.YELLOW + f"Model {friendly_name} failed. Trying next model...")
            continue
