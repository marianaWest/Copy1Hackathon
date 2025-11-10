from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
GPTKEY = os.getenv('GPTKEY')

client = OpenAI(api_key=GPTKEY)

response = client.responses.create(
    model="gpt-3.5-turbo",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)