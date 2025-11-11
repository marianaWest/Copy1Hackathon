from dotenv import load_dotenv
import os
from openai import OpenAI
import json



load_dotenv()
GPTKEY = os.getenv('GPTKEY')

client = OpenAI(api_key=GPTKEY)

with open("undefined_names.json", "r", encoding="utf-8") as f:
    undefined_names = json.load(f)

batch_size = 100

# check if photographer is likely female -- first try with only first 100 items
# for i in undefined(0, len(undefined), batch_size):
#     batch = undefined[i:i+batch_size]
    
#     for item in batch: 
#         if ():
#             probably_female.append(item)

probably_female = []

for i, item in enumerate(undefined_names[:30], 1):
    owner = item.get("Copyright owner", "")
    author = item.get("Copyright author of work", "")
    text_to_check = f"{owner} {author}"

    response = client.responses.create(
        model="gpt-3.5-turbo",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": f"Check if any female name appears in the following text: {text_to_check}. Reply only with 'yes' or 'no'."
                    },
                ],
            },
        ],
    )

    output_text = response.output[0].content[0].text.strip().lower()
    print(f"For item {i}, computer says {output_text}")

    if "yes" in output_text:
        probably_female.append(item)



print(len(probably_female))
