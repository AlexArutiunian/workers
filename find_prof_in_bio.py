import json

def update_occupations(json_data):
    for item in json_data:
        print(item)
        if 'occupations' not in item or not item['occupations'] and len(item["text"]):
            item['occupations'] = item['text'].split('\n')[0]

    return json_data

json_file_path = 'workers/data.json'

with open(json_file_path) as json_file:
    data = json.load(json_file)

updated_data = update_occupations(data)

print(json.dumps(updated_data, indent=4))

with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(updated_data, json_file, indent=2)