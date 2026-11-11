import json

# with open("salom.json") as ptr:
#     data = json.load(ptr)

#     for i in data:
#         if "matematika" in i["subjects"]:
#             print(i)

# # 2
# with open("salom.json") as ptr:
#     data=json.load(ptr)

#     for i in data:
#         jami=int(i["narx"])*int(i["soni"])

# print(jami)        

# 3
# with open("salom.json") as ptr:
#     data=json.load(ptr)
#     print(max(data,key=lambda x:x["soni"]))
       

# 4
# with open("salom.json") as ptr:
#     data=json.load(ptr)
#     for i in data:
#         if 1000>int(i["price"])>500 and i["is_available"]==True:
#             print(i)

# # 5
# with open("salom.json") as ptr:
#     data=json.load(ptr)
#     new=[]
#     for i in data:
#      if i["is_available"]==True:
#       new.append(i)

# print(sorted(new,key=lambda x:x["price"])) 


# 6
# with open("salom.json") as ptr:
#   data=json.load(ptr)
#   for i in data:
#     if int(i["price"])<1000 and i["is_available"]==False:
#        print(i)

# # 7
# with open("salom.json") as ptr:
#     data=json.load(ptr)
#     for i in data:
#             print(data)

# # 8
# with open("salom.json") as ptr:
#  data=json.load(ptr)
#  y=0
#  for i in data:
#     y+=int(i['yosh'])

# print(y)

# 9
# with open("salom.json") as ptr:
#     data=json.load(ptr)
#     for i in data["products"]:
#         print(int(i["price"]))

# # 10
# with open("salom.json") as ptr:
#     data=json.load(ptr)
#     a=max(data["people"],key=lambda x:len(x["name"]))
#     print(a["name"])

# 11
# with open("salom.json") as ptr:
#     data=json.load(ptr)
#     lst=[]
#     for i in data["contacts"]:
#         lst.append(i["phone"])
# print(lst)

# uy ishi 1

# with open("salom.json") as ptr:

#     data = json.load(ptr)

#     sum_price = 0
#     for user in data:
#         for item in user['items']:
#             sum_price += item['price'] * item['quantity']



#     print(f"Yakuniy narx : {sum_price}")


#     # 2-masala

#     max_price = -1
#     max_customer = data[0]['customer_name']
#     for user in data:
#         user_max = max(user['items'],key=lambda x: x['price'])

#         if user_max['price'] > max_price:
#             max_price = user_max['price']
#             max_customer = user['customer_name']


#     print(f"Max user : {max_customer} : {max_price}")

# # uy ishi 2
# with open("salom.json") as ptr:
#     data=json.load(ptr)
# pitsa=[i for i in data  if i["category"]=="Pizza"]
# arzon=min(pitsa,key=lambda x:x['price'])
# qimmat=max(pitsa,key=lambda x:x['price'])
# print("eng arzon pizza",arzon["name"],arzon['price'])
# print("Eng qimmat",qimmat['price'],qimmat["name"])

# # uy ishi 3
# with open("salom.json") as ptr:
#     data=json.load(ptr)
# chipta=[i for i in data if i["from"]=="Tashkent"]
# arzon=min(chipta,key=lambda x:x["price"])
# qimmat=max(chipta,key=lambda x:x["price"])

# print("eng arzoni:",arzon['flight'],arzon["to"],arzon['price'])
# print("Eng qimmati:",qimmat['flight'],qimmat['to'],qimmat['price'])
# jami=sum(i['seats'] for i in data)
# print("Umumiy orinlar",jami)


# # uy ishi 4
# with open("salom.json") as ptr:
#     data=json.load(ptr)
#     for i in data:
#         print(i["city"],i["temperature"],i["humidity"])
# issiq=max(data,key=lambda x:x["temperature"])
# sovuq=min(data,key=lambda x:x["temperature"])
# ortachasi=sum(i ["temperature"] for i in data) / len(data)
# print("eng issiq ",issiq['city'])
# print("eng sovuq ",sovuq['city'])
# print("Ortachasi ",ortachasi)

# #  5
# with open("salom.json") as ptr:
#     data=json.load(ptr)
#     lis=[]
#     # a=[i for i in data if i["courses"]=="python"]
#     for i in data:
#         # print(i["name"],i["age"],i["courses"])
#         if "Python" in i["courses"]:
#             lis.append(i["name"])

# print("Paytin oqiyatganlar",lis)            
# print(len(lis))



