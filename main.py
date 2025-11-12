import csv
import json
import re


csv.field_size_limit(10_000_000)

csv_file = "TNA_Search_Results_23-10-2025_child.csv"
search_results = "data/data.json"
columns_to_keep = ["Citable Reference", "Context Description", "Title", "Description", "Start Date"]
phrases_to_exclude = ["Josefine Stross", "Photographer: Unknown", "Photographer(s): Unknown", "Beato, Felice"]

filtered_rows = []

with open(csv_file, mode='r', encoding='utf-8', errors='ignore') as f:
    reader = csv.DictReader(f)
    for row in reader:
        filtered_row = {key: row[key] for key in columns_to_keep if key in row}
        if not any(
            phrase.lower() in str(value).lower()
            for phrase in phrases_to_exclude
            for value in filtered_row.values()
            ):
            filtered_rows.append(filtered_row)
    

        with open(search_results, mode='w', encoding='utf-8') as f:
            json.dump(filtered_rows, f, indent=4, ensure_ascii=False)


output_file = "data/search_results_parsed.json"

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

fields_to_check = ["Description", "Context Description", "Title"]

with open(search_results, "r", encoding="utf-8") as f:
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

# print(f"✅ Extracted all copyright and photographer info → {output_file} with {len(data)} items")



