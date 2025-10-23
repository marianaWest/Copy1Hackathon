import csv
import sys
import json

csv.field_size_limit(10_000_000)

csv_file = "TNA_Search_Results_23-10-2025_child.csv"
json_file = "data.json"
columns_to_keep = ["Citable Reference", "Context Description", "Title", "Description", "Start Date"]

filtered_rows = []

with open(csv_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        filtered_row = {key: row[key] for key in columns_to_keep if key in row}
        filtered_rows.append(filtered_row)

        with open(json_file, mode='w', encoding='utf-8') as f:
            json.dump(filtered_rows, f, indent=4)

            print(f"✅ Saved {len(filtered_rows)} rows with selected columns to {json_file}")
