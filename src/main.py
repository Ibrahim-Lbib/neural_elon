# entrypoint (CLI menu & mode switch)
import random
from generator.combo_generator import generate_startup_idea
from generator.persona import muskify
# from generator.saver import save_idea_to_vault

def print_banner():
    # ASCII banner or small art
    with open("assets/banner.txt", "r") as f:
        banner = f.read()
    print(banner)

def prompt_topic():
    topic = input("Enter a topic or industry: ")
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
        prompt_number_of_ideas()
    else:
        print("Invalid choice. Please try again.")
        prompt_mode()
    return mode

def prompt_number_of_ideas():
    try:
        ideas = int(input("How many startup ideas would you like to generate? "))
        print(f"You requested {ideas} ideas.")
        
    except:
        print("Please enter a valid number.")
        prompt_number_of_ideas()
    prompt_creativity_level()
    confirm_generation(ideas)

def prompt_creativity_level():
    try:
        level = int(input("Select creativity level (1-10): "))
        print(f"Creativity level set to {level}.")
        return level
    except:
        print("Please enter a valid number.")
        prompt_creativity_level()
    
def confirm_generation(ideas):
    confirm = input(f"Generate {ideas} startup ideas? (y/n): ")
    if confirm.lower() != 'y':
        print("Operation cancelled.")
        return
    elif confirm.lower() == 'y':
        print("Generating startup ideas...")
        display_ideas(ideas)
        
def display_ideas(ideas, topic, creativity):
    try:
        num_ideas = ideas
        print(f"-------------------------------")
        for i in range(num_ideas):
            idea = generate_startup_idea()
            persona_idea = muskify(idea)
            print(f"💡 Generated Startup Idea: {persona_idea}")            
            # print(f"💡 Generated Startup Idea: {idea}")
        print(f"-------------------------------")
        print()
        
        print("1. Save ideas to vault (y/n)")
        print("2. Generate more for same topic")
        print("3. Enter a new topic")
        print("0. Quit")
        
        choice = input("Please select an option: ")
        
        if choice == "1":
            print("Saving feature is not available")
            # append_ideas()
        elif choice == "2":
            print(f"-------------------------------")
            for i in range(num_ideas):
                idea = generate_startup_idea()
                persona_idea = muskify(idea)
                print(f"💡 Generated Startup Idea: {persona_idea}")
            print(f"-------------------------------")
            print()
        elif choice == "3":
            prompt_topic()
        elif choice == "0":
            print("Quiting the application... Goodbye!")
   
    except ValueError:
        print("Please enter a valid number.")

def start_application():
    print("Application is starting...")
    topic = prompt_topic()
    return topic

def main():
    while True:
        print_banner()
        print(f"""
===============================
🚀  Neural Elon v1.0 
The AI Brainstorm Buddy 
===============================
        """)
        print("1. Start Application")
        print("0. Exit")
        choice = input("Please select an option: ")
        
        if choice == '1':
            start_application()
        elif choice == '0':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            main() 
        
if __name__ == "__main__":
    main()