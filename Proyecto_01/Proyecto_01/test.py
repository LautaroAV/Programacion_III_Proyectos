from urllib.request import urlopen
import json

url = "https://digimon-api.vercel.app/api/digimon"
response = urlopen(url)
data = json.loads(response.read())

for i in data:
    print (i["name"])
