from urllib.request import urlopen
import json

url = "http://makeup-api.herokuapp.com/api/v1/products.json?product_type=Blush"
response = urlopen(url)
categorias_tags = json.loads(response.read())
for i in categorias_tags:
    for k in i["tag_list"]:
        if k == "Vegan":
            devolver_tag = i
            print (categorias_tags)