# save to idea_vault / file IO 
from pathlib import Path

def save_idea_to_vault():
    p = Path('data/idea_vault.txt')
    p.write_text(f"\nHello, World!")
    p.read_text()
    return p

save = save_idea_to_vault()
print(save)