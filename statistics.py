import json

res = {}

with open("workers_/data.json", "r", encoding="utf-8") as f:
    datas = json.load(f)
    for data in datas:
        label = data["occupations"]
        if label not in res:
            res[label] = 1
        else:
            res[label] += 1
print(res)