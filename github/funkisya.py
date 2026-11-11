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