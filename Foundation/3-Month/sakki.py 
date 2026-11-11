# 1

# ptr=open("salomlar.txt")
# data=ptr.read().split("\n")
# dct={}
# for qator in data:
#     bolak=qator.split(",")[-1]

#     if bolak not in dct:
#         dct[bolak] = 1
#     else:
#         dct[bolak] += 1

# print(dct)    


# 2

# ptr=open("salomlar.txt")
# st=set()
# for qator in ptr.read().split("\n")[1:]:
#     bolak=qator.split(",")
#     if "visa" in bolak[1]:
#         st.add(bolak[-1])
# print(sorted(st))

# ptr.close()


# # 3
# ptr=open("salomlar.txt")
# data=ptr.read().split("\n")
# st=set()
# for qator in data:
#     bolak=qator.split(",")
#     if len(set(bolak[0]))==10:
#         print(qator)

# ptr.close()        


# 2 masalnai 1

# ptr = open("salomlar.txt")

# data = ptr.read().split("\n")

# for qator in data:
#     bolak = qator.split(",")
#     mac = bolak[-2].split("-")
#     for i in mac:
#         if i.isdigit():
#             break
#     else:
#         print(bolak[0], bolak[-2])

# ptr.close()

# 2 masla 2
# with open("salomlar.txt") as ptr:
#     data = ptr.read().split("\n")
#     dct = {}
#     for i in data:
#         bolak = i.split(",")[0]
#         email = bolak.split(".")[-1]
        
#         if email not in dct:
#             dct[email] = 1
#         else:
#             dct[email] += 1
            
            
# print(dct)

# # 3 masala 1
# with open("salomlar.txt") as matn:
#     data=matn.read().split("\n")
#     dct={}
#     for i in data:
#         bolak=i.split(",")[-2]
#         yil = bolak.split("-")[-1]
#         if int(yil) >= 1950 and int(yil) <= 2005:
#             if yil not in dct:
#                 dct[yil] = 1
#             else:
#                 dct[yil] +=1
#     print(dct)
        


# uy ishi 1 masala

# with open("salomlar.txt") as fayl:
#     data = fayl.read().split("\n")

# brendlar = {}
# davlatlar = {}

# for i in data[1:]:
#     if i.strip() == "":
#         continue
#     b = i.split(",")
#     brend = b[4].strip()
#     davlat = b[7].strip()
#     brendlar[brend] = brendlar.get(brend, 0) + 1
#     if brend not in davlatlar:
#         davlatlar[brend] = {}
#     davlatlar[brend][davlat] = davlatlar[brend].get(davlat, 0) + 1

# eng_kop = max(brendlar, key=brendlar.get)
# d = davlatlar[eng_kop]

# print("Eng kop brend:", eng_kop, brendlar[eng_kop])
# print("Eng kop davlat:", max(d, key=d.get), d[max(d, key=d.get)])
# print("Eng kam davlat:", min(d, key=d.get), d[min(d, key=d.get)])

 


