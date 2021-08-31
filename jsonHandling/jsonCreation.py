#json libary
import json

#json dump --> to convert a python objecto to a Json File

x = {
  "name": "Carmikael",
  "age": 10,
  "married": False,
  "divorced": False,
  "children": None,
  "pets": None,
  "cars": None
}
with open("jsonHandling/myJson.json","w") as file:
    x = json.dumps(x)
    file.write(x)