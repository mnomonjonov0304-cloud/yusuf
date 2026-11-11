# import json
# with open("last.json") as ptr:
#     data=json.load(ptr)
#     new=[]
#     print(data["branches"])

# import json
# with open("last.json") as ptr:
#     data=json.load(ptr)
#     new=[]
#     for i in data["branches"]:
#         for x in i["teachers"]:
#             if x["subject"]=="Python":
#                 new.append({"branch":i["name"],"teacher_name":x["name"],"exesperense":x["experience"]})
# for i in new:
#     print(i)

# import json
# with open("last.json") as ptr:
#     data=json.load(ptr)
#     for i in data["branches"]:
#         print(i["name"],len(i["students"]))

# import json
# with open("last.json") as ptr:
#     data=json.load(ptr)
#     kotta=0
#     ism=""
#     fil=""
#     for i in data["branches"]:
#         for x in i["students"]:
#             if x["payment"]>kotta:
#                 kotta=x["payment"]
#                 ism=x["name"]
#                 fil=i["name"]
# print(kotta,ism,fil)                


