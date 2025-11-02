import requests
import dotenv
import os

dotenv.load_dotenv()
API_KEY = os.getenv("NEURAL_ELON_API_KEY")
API_URL = "https://api.openai.com/v1/chat/completions" 

data = requests.get
user_input = input("Enter your prompt for Neural Elon: ")


