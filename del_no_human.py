import json

def remove_items_with_link_for_arts(json_data):
    return [item for item in json_data if item.get('occupations', '') != '1']

json_file_path = 'workers_/data.json'

with open(json_file_path, "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

filtered_data = remove_items_with_link_for_arts(data)

print(json.dumps(filtered_data, indent=4))

with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(filtered_data, json_file, indent=2)