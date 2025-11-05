import gender_guesser.detector as gender
import json

detector = gender.Detector()
identification_keys = ["Copyright owner of work","Copyright author of work",  "Photographer",  "Photographer(s)", "Copyright owner and author of work", "Copyright owner(s) and author(s) of work"]


def detect_gender(name):
    print(detector.get_gender(name))

result = detect_gender('Mrs')
print(result)

with open("data_parsed.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# remove items without reference to photographer - might move somewhere else
no_photographer = [
    item for item in data
    if any(key in item for key in identification_keys)
]

print((len(no_photographer)))