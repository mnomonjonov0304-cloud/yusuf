def majority_element(nums: list) -> int:
    if len(nums) == 0:
        return -1

    sanoq = {}
    for i in nums:
        if i in sanoq:
            sanoq[i] += 1
        else:
            sanoq[i] = 1

    eng_k = 0
    javob = -1
    for son in sanoq:
        if sanoq[son] > eng_k:
            eng_k = sanoq[son]
            javob = son

    return javob
def search_by_genre(cinema: list, genre: str) -> list:
    natija=[]
    for film in cinema:
        if film["genre"]==genre:
            natija.append(film)
    return natija

def merge_unique_ids(active_users: list, new_users: list) -> list:
    natija = []
    for i in active_users:
        if i not in natija:
            natija.append(i)
    for i in new_users:
        if i not in natija:
            natija.append(i)
    return natija



