def solution(clothes):
    temp = 1
    ndict = dict()
    for cloth in clothes:
        if cloth[1] not in ndict:
            ndict[cloth[1]] = 2
        else:
            ndict[cloth[1]] += 1
    for value in ndict.values():
        temp *= value
    return temp - 1
