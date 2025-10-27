import json
import re

input_file = "data.json"
output_file = "data_parsed.json"

# Patterns for different copyright and photographer labels
pattern_groups = {
    "Copyright owner of work": [
        r"Copyright owner of work:\s*([^.\n]+)",
        r"Copyright owner(?:\(s\))? of work:\s*([^.\n]+)",
        r"inscribed\s+['\"]?Copyright[,:\s]+([^.'\"\n]+)",
        r"Copyright[,:\s]+([^.\n]+)"
    ],
    "Copyright author of work": [
        r"Copyright author of work:\s*([^.\n]+)",
        r"Copyright author(?:\(s\))? of work:\s*([^.\n]+)"
    ],
    "Photographer": [
        r"Photographer(?:\(s\))?:\s*([^.\n]+)",
        r"Photographers?:\s*([^.\n]+)"
    ],
    "Photographer(s)": [
        r"Photographer\(s\):\s*([^.\n]+)",
        r"Photographer(?:\(s\))?:\s*([^.\n]+)"
    ],
    "Copyright owner and author of work": [
        r"Copyright owner and author of work:\s*([^.\n]+)",
        r"Copyright owner(?:\(s\))? and author(?:\(s\))? of work:\s*([^.\n]+)"
    ],
    "Copyright owner(s) and author(s) of work": [
        r"Copyright owner\(s\) and author\(s\) of work:\s*([^.\n]+)",
        r"Copyright owner(?:\(s\))? and author(?:\(s\))? of work:\s*([^.\n]+)"
    ],
}

# Fields to check
fields_to_check = ["Description", "Context Description", "Title"]

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    for field_name in fields_to_check:
        text = item.get(field_name, "")
        if not text:
            continue

        for key, regex_list in pattern_groups.items():
            for pattern in regex_list:
                matches = re.findall(pattern, text, re.IGNORECASE)
                for match in matches:
                    found = match.strip()
                    found = re.sub(r"\s+", " ", found).rstrip(" ,.")
                    existing = item.get(key, "")
                    if existing:
                        item[f"{key} ({field_name})"] = f"{existing}; {found}"
                    else:
                        item[key] = found

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"✅ Extracted all copyright and photographer info → {output_file} with {len(data)} items")
