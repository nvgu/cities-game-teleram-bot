import json
with open('cities.json', encoding="utf8") as json_data:
    d = json.load(json_data)
    print(d)
