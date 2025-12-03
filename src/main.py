# entrypoint (CLI menu & mode switch)
from colorama import Fore, Back, Style, init
from src.generator.combo_generator import generate_startup_idea
from src.generator.persona import muskify
from src.generator.saver import save_idea_to_vault, save_multiple_ideas_to_vault

init() # Initialize colorama

def print_banner():
    # ASCII banner 
    with open("assets/banner.txt", "r") as f:
        banner = f.read()
    print(Fore.GREEN + banner)

def prompt_topic():
    while True:
        topic = input("Enter a topic or industry: ").strip()
        if topic.lower() == "q":
            return None
        if topic and len(topic) <= 100: # Prevent overly long inputs
            print(f"You entered: {topic}")
            return topic
        print("❌ Topic cannot be empty or too long (max 100 chars).")

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
            try:
                from src.ai.api_client import check_api_key
                check_api_key()
                print("🤖 AI-Enhanced mode selected.")
                return "AI-Enhanced"
            except Exception as e:
                print("AI module not found. Switching to Offline mode.")
                print(f"Error: {e}")
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
    
def confirm_generation(topic, mode, num_ideas, creativity):
    confirm = input(f"Generate {num_ideas} startup ideas for '{topic}'? (y/n): ").strip().lower()
    if confirm == 'y':
        print("Generating startup ideas...")
        return True
    else:
        print("Operation cancelled.")
        return False
        
def display_ideas(topic, mode, num_ideas, creativity):
    try:
        print(f"-------------------------------")
        ideas_generated = []
        ideas_count = 0
        
        try:
            if  mode == "AI-Enhanced":
                from src.ai.api_client import generate_ideas
                print(Fore.GREEN + "Neural Elon is thinking deeply...")               
                ideas_generated = generate_ideas(topic, num_ideas, creativity)
            else:
                ideas_generated = []
                for i in range(num_ideas):
                    idea = generate_startup_idea(topic, mode, num_ideas, creativity)
                    if idea: # Check if idea was generated
                        persona_idea = muskify(idea)
                        print(f"💡 Generated Startup Idea {i+1}: {persona_idea}") 
                        ideas_generated.append(persona_idea)
                        ideas_count += 1
                
        except Exception as e:
            print(f"❌ Failed to generate idea {i+1}: {e}")
        if ideas_count == 0:
            print("No ideas were generated. Please try different parameters.")
            return "error"
            
        print(f"-------------------------------")
        print()
        
        while True:
            try:
                print("What would you like to do?")
                print("1. Save ideas to vault (y/n)")
                print("2. Generate more for same topic")
                print("3. Enter a new topic")
                print("0. Quit")
                choice = input("Please select an option: ").strip()
                
                if choice.lower() == "y" or choice == "1":
                    print("\n💾 Save Options:")
                    print("1. Saving all generated ideas")
                    print("2. Save a specific idea")
                    print("0. Cancel")
                    save_choice = input("Choose an option: ").strip()
                    
                    if save_choice == "1":
                        print("\n💾 Saving all ideas to vault...")
                        save_multiple_ideas_to_vault(ideas_generated)
                        print(f"✅ Successfully saved {len(ideas_generated)} ideas!")
                    elif save_choice == "2":
                        print("\nSelect the idea number to save:")
                        for idx, idea in enumerate(ideas_generated, start=1):
                            print(f"{idx}. {idea}")
                        try:
                            idea_choice = int(input("Enter idea number: ")) - 1
                            if 0 <= idea_choice < len(ideas_generated):
                                save_idea_to_vault(ideas_generated[idea_choice])
                            else:
                                print("Invalid idea number.")
                        except ValueError:
                            print("Please enter a valid number.")
                    elif save_choice == "0":
                        print("Save operation cancelled.")
                        return
                    else:
                        print(Fore.RED + "Invalid choice. Please try again.")
                        print(Style.RESET_ALL)
                        
                elif choice.lower() == "n":
                    print("Ideas not saved.")
                elif choice == "2":
                    return "regenerate"
                elif choice == "3":
                    return "new_topic"
                elif choice == "0":
                    print("Quiting the application... Goodbye!")
                    return "quit"
                else:
                    print("Invalid choice. Please try again.")
                    
            except KeyboardInterrupt:
                print("\nOperation cancelled by user.")
                break
        
    except ValueError:
        print("Please enter a valid number.")
        return "error"

def start_application():
    while True:
        print("Application is starting...")
        topic = prompt_topic()
        if topic is None:
            print("Exiting to main menu.")
            return
        mode = prompt_mode()
        num_ideas = prompt_number_of_ideas()  
        creativity = prompt_creativity_level()
        
        if confirm_generation(topic, mode, num_ideas, creativity):
            result = display_ideas(topic, mode, num_ideas, creativity)
            
            if result == "regenerate":
                continue # Regenerate with same parameters
            elif result == "new_topic":
                continue # Start new topic
            elif result == "quit":
                break

def main():
    while True:
        print_banner()
        print(Style.RESET_ALL + f"""
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