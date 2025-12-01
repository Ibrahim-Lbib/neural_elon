# offline/random-combo logic
import random
import os

def load_list_from_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        
    items = []
    for line in lines:
        cleaned_line = line.strip()
        if cleaned_line:
            items.append(cleaned_line)
    
    return items

def generate_startup_idea(topic, mode, num_ideas, creativity):
    industries = load_list_from_file(os.path.join("data", "wordlists", "industries.txt"))
    techs = load_list_from_file(os.path.join("data", "wordlists", "techs.txt"))
    concepts = load_list_from_file(os.path.join("data", "wordlists", "concepts.txt"))
    goals = load_list_from_file(os.path.join("data", "wordlists", "goals.txt"))
    
    ideas = []
    
    for i in range(num_ideas):
        industry = topic if topic and topic.lower() != "random" else random.choice(industries)
        
        tech = random.choice(techs)
        concept = random.choice(concepts)
        goal = random.choice(goals)
        
        idea = f"A {tech} {concept} in the {industry} industry that aims to {goal}."
        ideas.append(idea)
    
    return ideas[-1] if ideas else "A revolutionary idea in " + industry 