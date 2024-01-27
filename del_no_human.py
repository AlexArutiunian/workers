import json

def remove_items_with_link_for_arts(json_data):
    return [item for item in json_data if item.get('link_for_arts', '') != '1']

json_file_path = 'workers/data.json'

with open(json_file_path) as json_file:
    data = json.load(json_file)

filtered_data = remove_items_with_link_for_arts(data)

print(json.dumps(filtered_data, indent=4))