# save to idea_vault / file IO 
from pathlib import Path

def save_idea_to_vault(idea):
    Path('data').mkdir(exist_ok=True)
    
    with open('data/idea_vault.txt', 'a', encoding='utf-8') as f:
        f.write(idea + "\n")
        
    print(f"✓ Saved: {idea}")

def save_multiple_ideas_to_vault(ideas):
    Path('data').mkdir(exist_ok=True)
    
    with open('data/idea_vault.txt', 'a', encoding='utf-8') as f:
        for idea in ideas:
            f.write(idea + "\n")
            
    print(f"✓ Saved {len(ideas)} ideas to idea_vault.")
