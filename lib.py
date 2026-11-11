def toliq(sana:str):
    kun=sana.split('.')[0]
    oy=sana.split('.')[1]
    yil=sana.split('.')[2]
    if oy=='01'and 1<int(kun)<31:
        print(f"{kun} yanvar {yil} yil.")
    elif oy=='02' and 1<int(kun)<28:
        print(f"{kun} fevral {yil} yil.")
    elif oy=='03' and 1<int(kun)<31:
            print(f"{kun} mart {yil} yil.")
    elif oy=='04' and 1<int(kun)<30:
            print(f"{kun} aprel {yil} yil.")
    elif oy=='05' and 1<int(kun)<31:
            print(f"{kun} may {yil} yil.")
    elif oy=='06' and 1<int(kun)<30:
            print(f"{kun} iyun {yil} yil.")
    elif oy=='07' and 1<int(kun)<31:
            print(f"{kun} iyul {yil} yil.")
    elif oy=='08' and 1<int(kun)<31:
            print(f"{kun} avgust {yil} yil.")
    elif oy=='09' and 1<int(kun)<30:
            print(f"{kun} sentabr {yil} yil.")
    elif oy=='10' and 1<int(kun)<31:
            print(f"{kun} oktobr {yil} yil.")
    elif oy=='11' and 1<int(kun)<30:
            print(f"{kun} nayabr {yil} yil.")
    elif oy=='12' and 1<int(kun)<31:
            print(f"{kun} dekabr {yil} yil.")


def uzer(data):
       user={}
       for name ,score in data:
              user[name] = user.get(name, 0) + score
       if not user :
              return ""
       return max(user,key=user.get)

def talab(grades,i):
       count=0
       for i in grades:
              if i>=60:
                count+=1
                
       return count   


def ends_with_gram(words: list[str]) -> list[str]:
    return [word for word in words if word.lower().endswith("gram")]    




# uy ishi 1
def toliq(sana:str):
    kun=sana.split('.')[0]
    oy=sana.split('.')[1]
    yil=sana.split('.')[2]
    if oy=='01'and 1<int(kun)<31:
        print(f"{kun} yanvar {yil} yil.")
    elif oy=='02' and 1<int(kun)<28:
        print(f"{kun} fevral {yil} yil.")
    elif oy=='03' and 1<int(kun)<31:
            print(f"{kun} mart {yil} yil.")
    elif oy=='04' and 1<int(kun)<30:
            print(f"{kun} aprel {yil} yil.")
    elif oy=='05' and 1<int(kun)<31:
            print(f"{kun} may {yil} yil.")
    elif oy=='06' and 1<int(kun)<30:
            print(f"{kun} iyun {yil} yil.")
    elif oy=='07' and 1<int(kun)<31:
            print(f"{kun} iyul {yil} yil.")
    elif oy=='08' and 1<int(kun)<31:
            print(f"{kun} avgust {yil} yil.")
    elif oy=='09' and 1<int(kun)<30:
            print(f"{kun} sentabr {yil} yil.")
    elif oy=='10' and 1<int(kun)<31:
            print(f"{kun} oktobr {yil} yil.")
    elif oy=='11' and 1<int(kun)<30:
            print(f"{kun} nayabr {yil} yil.")
    elif oy=='12' and 1<int(kun)<31:
            print(f"{kun} dekabr {yil} yil.")



# uy ishi 2
def get_top_user(data: list[tuple[str, int]]) -> str:
    if not data:
        return ""

    scores = {}

    for userid, score in data:
        if userid in scores:
            scores[userid] += score
        else:
            scores[userid] = score

    return max(scores, key=scores.get)


# uy ishi 3
def maktab(scores: dict) -> dict:
    result = {}

    for class_name, marks in scores.items():
        if len(marks) == 0:
            result[class_name] = 0
        else:
            average = sum(marks) / len(marks)

            whole = int(average)

            if average - whole > 0.5:
                whole += 1

            result[class_name] = whole

    return result
# uy ishi 42m
def kotta(movies: list) -> tuple:
    if not movies:
        return (0, [])

    movies = sorted(movies, key=lambda x: x[1])

    selected = []
    last_end = 0

    for start, end in movies:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return (len(selected), selected)

             
            