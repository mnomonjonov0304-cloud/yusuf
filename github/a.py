import json
with open("last.json") as ptr:
    data=json.load(ptr)
    new=[]
    print(data["branches"])

