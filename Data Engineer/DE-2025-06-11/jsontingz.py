# JSONTINGZ

import json

item = {
    "name": "Book of bro knowledge",
    "rarity": "Tier 10 type shit",
    "durability": 100,
    "bookmark-page": 55,
 }

json_string = json.dumps(item, indent=2)
print(json_string)

with open("item.json", "w") as file:
    json.dump(item, file, indent=2)

with open("item.json", "r") as file:
    loaded_item = json.load(file)

print("Name:", loaded_item["name"])
print("Bookmark-page:", loaded_item["bookmark-page"])

    