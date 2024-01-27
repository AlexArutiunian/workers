import json

def update_occupations(json_data):
    for item in json_data:
        if 'occupations' not in item or not item['occupations']:
            item['occupations'] = item['text'].split('\n')[0]

    return json_data

json_file_path = 'data.json'

with open(json_file_path) as json_file:
    data = json.load(json_file)

updated_data = update_occupations(data)

print(json.dumps(updated_data, indent=4))