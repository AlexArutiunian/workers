import json
from bs4 import BeautifulSoup

with open("site.txt", "r", encoding="utf-8") as file:
    site = file.read()

soup = BeautifulSoup(site, "html.parser")

tr2 = soup.find_all("tr")
tr = []
for i, tag_tr in enumerate(tr2):
    if i != 0:
        tr.append(tag_tr)
        
print(len(tr))
all_sides_links = []
names = []
datas = []
for t in tr:
    tag_a = t.find_all("a")
    name = tag_a[0].get_text()
    bans = ["The", "News", "Online", "New", ".com", "Journal",
            "CNN", "Daily", "Business", "Time", "Week", "Today", 
            "view", "Report", "Institut", "Radio", "Magazine", "Polit",
            "Public", "Foreign", "Press"]
    if (any(item in name for item in bans) or len(name.split()) != 2 
        or any(char.isnumeric() for char in name)):
        continue
    data = {
        "name": tag_a[0].get_text(),
        "bias": tag_a[1].get("href").replace("/media-bias/", ""),
        "allsides_link": "https://www.allsides.com" + tag_a[0].get("href"),
        "occupations": "",
        "bio": "" 
    }
    print(data)
    datas.append(data)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(datas, f, indent=2)