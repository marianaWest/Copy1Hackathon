from dotenv import load_dotenv
import os

# Load environment variables from the .env file (if present)
load_dotenv()

GPT_KEY = os.getenv('GPT_KEY')
