import csv
import json
import re
import gender_guesser.detector as gender


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


detector = gender.Detector()
identification_keys = ["Copyright owner of work","Copyright author of work",  "Photographer",  "Photographer(s)", "Copyright owner and author of work", "Copyright owner(s) and author(s) of work"]
female_honorifics = ["miss ", "miss.", "mrs", "mrs. ", "ms. ", "lady", "madame", "dame ", "madam"]
female_by_honorific = []
non_female_by_honorific = []
female_by_name = []
undefined_by_name = []
undefined_by_name_honorifics = []

with open(output_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# remove items without reference to photographer 
with_photographer = [
    item for item in data
    if any(key in item for key in identification_keys)
    ]


# checks for honorifics
for item in with_photographer:
    found = False

    for key in identification_keys:
        if key in item and isinstance(item[key], str):
            text = item[key].lower()
            if any(title in text for title in female_honorifics):
                female_by_honorific.append(item)
                found = True
                break

    if not found:
        non_female_by_honorific.append(item)


# checks for first name that appears 
for item in non_female_by_honorific:
    found = False

    for key in identification_keys:
        if key in item and isinstance(item[key], str):
            name = item.get(key)
            if name:
                first_name = name.split()[0]
                gender_result = detector.get_gender(first_name)
                if gender_result in ("female", "mostly_female"): 
                    female_by_name.append(item)
                    found = True
                    break
    
    if not found: 
        undefined_by_name.append(item)


female_honorific_name = female_by_honorific.copy()

for item in female_by_name:
    if item not in female_honorific_name:
        female_honorific_name.append(item)

with open("data/female_honorific_name.json", "w", encoding="utf-8") as f:
    json.dump(female_honorific_name, f, indent=4, ensure_ascii=False)

for item in with_photographer:
    if item not in female_honorific_name:
        undefined_by_name_honorifics.append(item)

with open("data/undefined_list.json", "w", encoding="utf-8") as f:
    json.dump(undefined_by_name_honorifics, f, indent=4, ensure_ascii=False)

print(f"Number of items with female names: {len(female_honorific_name)}")

