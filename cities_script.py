import json
with open('cities.json', encoding="utf8") as json_data:
    data = json.load(json_data)
    list_of_cities = data['city']
    city = list_of_cities