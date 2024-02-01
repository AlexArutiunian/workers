import json 

path = "workers_/occupations.json"

with open(path, "r", encoding="utf-8") as f:
    datas = json.read()
    for data in datas:
        if data.get("wiki"):
            continue
        else:
            data["wiki"] == ""

