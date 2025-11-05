import gender_guesser.detector as gender
import json

detector = gender.Detector()
identification_keys = ["Copyright owner of work","Copyright author of work",  "Photographer",  "Photographer(s)", "Copyright owner and author of work", "Copyright owner(s) and author(s) of work"]
female_honorifics = ["miss ", "miss.", "mrs","ms. ", "lady", "madame", "dame ", "madam"]
female_by_honorific = []
gender_by_name = []

with open("data_parsed.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# remove items without reference to photographer - might move somewhere else
with_photographer = [
    item for item in data
    if any(key in item for key in identification_keys)
]

def detect_gender(name):
    print(detector.get_gender(name))

result = detect_gender('Mrs')
print(result)



# checks for honorifics
for item in with_photographer:
    for key in identification_keys:
        if key in item and isinstance(item[key], str):
            text = item[key].lower()
            if any(title in text for title in female_honorifics):
                female_by_honorific.append(item)
                break

print(len(female_by_honorific))

with open("female_by_honorific", "w", encoding="utf-8") as f:
    json.dump(female_by_honorific, f, indent=4, ensure_ascii=False)