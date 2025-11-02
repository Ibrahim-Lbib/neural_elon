# entrypoint (CLI menu & mode switch)
import random

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

def start_application():
    print("Application is starting...")
    
    # Placeholder for actual application logic
    propmt = input("Enter a topic industry: ")
    print(f"You entered: {propmt}")
    
    mode = input("Select mode (1: Basic, 2: Advanced): ")
    
    if mode == '1':
        print("Basic mode selected.")
    elif mode == '2':
        print("Advanced mode selected.")
        for i in range(3):
            idea = generate_startup_idea()
            print(f"💡 Generated Startup Idea: {idea}")
        print()
    
    # ...
    # print("Application has started successfully.")

def main():
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