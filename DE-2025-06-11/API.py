import requests
import sys

kattig_fakta = []
for _ in range(5):
    response = requests.get("https://catfact.ninja/fact")
    data = response.json()
    kattig_fakta.append(data["fact"])

for fact in kattig_fakta:
    print(fact)
