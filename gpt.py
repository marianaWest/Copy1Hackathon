from dotenv import load_dotenv
import os
from openai import OpenAI
import json

load_dotenv()
GPTKEY = os.getenv('GPTKEY')

client = OpenAI(api_key=GPTKEY)

with open("undefined.json", "r", encoding="utf-8") as f:
    undefined = json.load(f)


response = client.responses.create(
    model="gpt-3.5-turbo",
       input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                   "text": f"Here is a list:\n{undefined}\nHow many items does it have?",
                },
               
            ]
        }
    ]
)

print(response.output_text)