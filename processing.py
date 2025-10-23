import csv
import sys
import json

csv.field_size_limit(10_000_000)

csv_file = "TNA_Search_Results_23-10-2025_child.csv"
json_file = "data.json"
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
    

        with open(json_file, mode='w', encoding='utf-8') as f:
            json.dump(filtered_rows, f, indent=4, ensure_ascii=False)

            print(f"✅ Saved {len(filtered_rows)} rows with selected columns to {json_file}")
