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

female_AI = []

for i, item in enumerate(undefined_names[:10], 1):
    owner = item.get("Copyright owner", "")
    author = item.get("Copyright author of work", "")
    text_to_check = f"{owner} {author}"

    response = client.responses.create(
        model="gpt-3.5-turbo",
        temperature=0,
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "Return only one word: 'Yes' if a clearly female name appears in the text below; otherwise, return 'No'. Do not include any explanation.\n\n"
                         f"Text: {text_to_check}"
                    },
                ],
            },
        ],
    )

    output_text = response.output[0].content[0].text.strip().lower()
    print(f"For item {i}, computer says {output_text}")

    if "yes" in output_text:
        female_AI.append(item)

print(len(female_AI))

with open("female_AI.json", "w", encoding="utf-8") as f:
    json.dump(female_AI, f, indent=4, ensure_ascii=False)
