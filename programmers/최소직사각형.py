def solution(sizes):
    w = 0
    l = 0
    for i, j in sizes:
        if i >= j:
            if w < i: w = i
            if l < j: l = j
        else:
            if w < j: w = j
            if l < i: l = i

    return w * l