import gender_guesser.detector as gender
import json

detector = gender.Detector()
identification_keys = ["Copyright owner of work","Copyright author of work",  "Photographer",  "Photographer(s)", "Copyright owner and author of work", "Copyright owner(s) and author(s) of work"]
female_honorifics = ["miss ", "miss.", "mrs", "mrs. ", "ms. ", "lady", "madame", "dame ", "madam"]
female_by_honorific = []
non_female_by_honorific = []
female_by_name = []
undefined_by_name = []
undefined = []

with open("data_parsed.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# remove items without reference to photographer - might move somewhere else
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

# with open("female_by_honorific.json", "w", encoding="utf-8") as f:
#     json.dump(female_by_honorific, f, indent=4, ensure_ascii=False)

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

# with open("female_by_name.json", "w", encoding="utf-8") as f:
#     json.dump(female_by_name, f, indent=4, ensure_ascii=False)

female_honorific_name = female_by_honorific.copy()

for item in female_by_name:
    if item not in female_honorific_name:
        female_honorific_name.append(item)

# with open("female_honorific_name.json", "w", encoding="utf-8") as f:
#     json.dump(female_honorific_name, f, indent=4, ensure_ascii=False)


# with open("undefined.json", "w", encoding="utf-8") as f:
#     json.dump(undefined_by_name, f, indent=4, ensure_ascii=False)

# print(f"All items with photographers: {len(with_photographer)}, female by honorific: {len(female_by_honorific)}, female by name: {len(female_by_name)}, combined list: {len(female_honorific_name)}, undefined by name: {len(undefined_by_name)}")


for item in with_photographer:
    if item not in female_honorific_name:
        undefined.append(item)

with open("undefined.json", "w", encoding="utf-8") as f:
    json.dump(undefined, f, indent=4, ensure_ascii=False)

print(f"items in undefined: {len(undefined)}")
