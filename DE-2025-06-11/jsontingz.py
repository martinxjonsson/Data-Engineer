# JSONTINGZ

import json

person = {
    "name": "Martin Jonsson",
    "age": 34,
    "skills": ["Python", "SQL", "Data"],
 }


json_string = json.dumps(person, indent=2)
print(json_string)