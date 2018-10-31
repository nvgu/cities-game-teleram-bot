import json
with open('cities.json') as json_data:
    d = json.load(json_data)
    print(d)