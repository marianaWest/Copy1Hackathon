import json
import re

input_file = "data.json"
output_file = "data_parsed.json"


patterns = {
    "Copyright owner of work": r"Copyright owner of work:\s*([^\.]+)",
    "Copyright author of work": r"Copyright author of work:\s*([^\.]+)",
    "Photographer": r"Photographer:\s*([^\.]+)",
    "Photographer(s)": r"Photographer(s):\s*([^\.]+)",
    "Copyright owner and author of work": r"Copyright owner and author of work:\s*([^\.]+)",
    "Copyright owner(s) and author(s) of work": r"Copyright owner(s) and author(s) of work:\s*([^\.]+)",
}

# must do the same for fields "Context Description" and "Title"
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    desc = item.get("Description", "")
    
    for key, pattern in patterns.items():
        match = re.search(pattern, desc, re.IGNORECASE)
        if match:
            # Add the extracted text as a new field
            item[key] = match.group(1).strip()
    

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"✅ Extracted copyright and photographer info into new fields → {output_file}")
