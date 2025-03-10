import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Function to get API key
def get_openai_api_key():
    if not OPENAI_API_KEY:
        raise ValueError("OpenAI API key not found! Set OPENAI_API_KEY in the .env file or environment variables.")
    return OPENAI_API_KEY
