# entrypoint (CLI menu & mode switch)
import random

def print_banner():
    # ASCII banner or small art
    with open("assets/banner.txt", "r") as f:
        banner = f.read()
    print(banner)
        

industries = ["transportation", "education", "energy", "medicine", "space", "AI", "agriculture"]
techs = ["quantum", "AI-powered", "solar", "autonomous", "blockchain", "neural", "drone-based", "fusion"]
concepts = ["platform", "network", "device", "service", "ecosystem", "infrastructure", "colony"]
goals = ["eliminate poverty", "make Mars livable", "remove human error", "extend life", "build faster cities"]

def generate_startup_idea():
    industry = random.choice(industries)
    tech = random.choice(techs)
    concept = random.choice(concepts)
    goal = random.choice(goals)
    
    idea = f"A {tech} {concept} in the {industry} industry that aims to {goal}."
    return idea

def prompt_topic():
    topic = input("Enter a topic industry: ")
    print(f"You entered: {topic}")
    prompt_mode()
    return topic

def prompt_mode():
    print("Select Mode:")
    print("1. Offline")
    print("2. AI-Enhanced")
    mode = input("Enter mode (1 or 2): ")
    
    if mode == '1':
        print("Offline mode selected.")
        prompt_number_of_ideas()
    elif mode == '2':
        print("AI-Enhanced mode selected.")
        print("AI unavailable. Switching to Offline mode.")
    return mode

def prompt_number_of_ideas():
    ideas = input("How many startup ideas would you like to generate? ")
    confirm_generation(ideas)
    
def confirm_generation(ideas):
    confirm = input(f"Generate {ideas} startup ideas? (y/n): ")
    if confirm.lower() != 'y':
        print("Operation cancelled.")
        return
    elif confirm.lower() == 'y':
        print("Generating startup ideas...")
        display_ideas(ideas)
        
def display_ideas(ideas):
    try:
        num_ideas = int(ideas)
        print(f"-------------------------------")
        for i in range(num_ideas):
            idea = generate_startup_idea()
            print(f"💡 Generated Startup Idea: {idea}")
        print(f"-------------------------------")
        print()
    except ValueError:
        print("Please enter a valid number.")

def start_application():
    print("Application is starting...")
    print_banner()
    topic = prompt_topic()
    return topic

def main():
    print_banner()
    while True:
        print(f"===============================\n🚀  Neural Elon v1.0 \nThe AI Brainstorm Buddy \n===============================")
        print("1. Start Application")
        print("2. Exit")
        choice = input("Please select an option: ")
        
        if choice == '1':
            start_application()
        elif choice == '2':
            print("Exiting the application. Goodbye!")
        else:
            print("Invalid choice. Please try again.")
            main() 
        
if __name__ == "__main__":
    main()