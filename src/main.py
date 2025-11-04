# entrypoint (CLI menu & mode switch)
from generator.combo_generator import generate_startup_idea
from generator.persona import muskify
# from generator.saver import save_idea_to_vault

def print_banner():
    # ASCII banner or small art
    with open("assets/banner.txt", "r") as f:
        banner = f.read()
    print(banner)

def prompt_topic():
    while True:
        topic = input("Enter a topic or industry: ").strip()
        if topic.lower() == "q":
            return None
        if topic:
            print(f"You entered: {topic}")
            return topic
        print("❌ Topic cannot be empty. Please try again.")

def prompt_mode():
    while True:
        print("Select Mode:")
        print("1. Offline")
        print("2. AI-Enhanced")        
        choice = input("Enter mode (1 or 2): ").strip()
                
        if choice == "1":
            print("🧠 Offline mode selected.")
            return "Offline"
        elif choice == "2":
            print("🤖 AI-Enhanced mode selected.")
            print("AI module not found. Switching to Offline mode.")
            return "Offline"
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")            

def prompt_number_of_ideas():
    while True:
        try:
            num = int(input("How many startup ideas would you like to generate? "))
            print(f"You requested {num} ideas.")
            if num > 0:
                return num
            print("Please enter a positive nume.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def prompt_creativity_level():
    while True:
        try:
            level = int(input("Select creativity level (1-10): "))
            print(f"Creativity level set to {level}.")
            if 1 <= level <= 10:
                return level
            print("Please enter a number between 1 and 10.")
        except:
            print("Invalid input. Please enter a number.")
    
def confirm_generation(num_ideas, topic, creativity):
    confirm = input(f"Generate {num_ideas} startup ideas? (y/n): ")
    if confirm.lower() != 'y':
        print("Operation cancelled.")
        return
    elif confirm.lower() == 'y':
        print("Generating startup ideas...")
        display_ideas(num_ideas, topic, creativity)
        
def display_ideas(num_ideas, topic, creativity):
    try:
        num = num_ideas
        print(f"-------------------------------")
        for i in range(num):
            idea = generate_startup_idea(num_ideas, topic, creativity)
            persona_idea = muskify(idea)
            print(f"💡 Generated Startup Idea: {persona_idea}") 
        print(f"-------------------------------")
        print()
        
        while True:
            try:
                print("1. Save ideas to vault (y/n)")
                print("2. Generate more for same topic")
                print("3. Enter a new topic")
                print("0. Quit")
                choice = input("Please select an option: ")
                
                if choice.lower() == "y" or choice == "1":
                    print("Feature not implemented yet.")
                    # save_idea_to_vault(ideas)
                elif choice.lower() == "n":
                    print("Ideas not saved.")
                elif choice == "2":
                    print(f"-------------------------------")
                    for i in range(num):
                        idea = generate_startup_idea(num_ideas, topic, creativity)
                        persona_idea = muskify(idea)
                        print(f"💡 Generated Startup Idea: {persona_idea}")
                    print(f"-------------------------------")
                    print()
                elif choice == "3":
                    prompt_topic()
                elif choice == "0":
                    print("Quiting the application... Goodbye!")
            except KeyboardInterrupt:
                print("\nOperation cancelled by user.")
                break
        
    except ValueError:
        print("Please enter a valid number.")

def start_application():
    print("Application is starting...")
    topic = prompt_topic()
    if topic is None:
        print("Exiting to main menu.")
        return
    mode = prompt_mode()
    num_ideas = prompt_number_of_ideas()  
    creativity = prompt_creativity_level()
    confirm_generation(num_ideas, topic, creativity)

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
        
if __name__ == "__main__":
    main()