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

# import json
# with open("last.json") as ptr:
#     data=json.load(ptr)
#     for i in data["branches"]:
#         umumiy=0
#         for x in i["students"]:
#             umumiy+=x["payment"]
#         print(i["name"],umumiy)   
#      
# import json
# with open("last.json") as ptr:
#     data=json.load(ptr)
#     for i in data["branches"]:
#         for x in i["teachers"]:
#           if x["experience"]>5:
#             print(x)

# import json
# with open("last.json") as ptr:
#       data = json.load(ptr)
#       for i in data["branches"]:
#             for x in i["students"]:
#                 if x["course"]=="Python":
#                      print(x["name"])


# uy ishi 
# from funkisya import majorty_element

# print(majorty_element([3, 3, 4]))
# print(majorty_element([1, 1, 2, 2, 2, 3]))
# print(majorty_element([]))

# uy ishi 2
# from funkisya import search_by_genre
# cinema = [
#     {"title": "Avatar", "genre": "Fantastika", "price": 40000},
#     {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
#     {"title": "Oq yo‘l", "genre": "Drama", "price": 25000},
#     {"title": "Dune", "genre": "Fantastika", "price": 35000}
# ]
# print(search_by_genre(cinema, "Fantastika"))
# print(search_by_genre(cinema, "Drama"))
# print(search_by_genre(cinema, "Komediya"))
# print(search_by_genre([], "Boevik"))
# print(search_by_genre(cinema, "Detektiv"))


# from funkisya import merge_unique_ids

# active_users = ['U1001', 'U1002', 'U1003', 'U1004', 'U1001']
# new_users = ['U1003', 'U1005', 'U1006', 'U1002', 'U1007']

# print(merge_unique_ids(active_users, new_users))
