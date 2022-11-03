def solution(citations):
    answer = 0
    h, n = 0, len(citations)
    while h <= n:
        up, down = 0, 0
        h += 1
        for i in range(len(citations)):
            if h <= citations[i]:
                up += 1
            else: down += 1
        if up >= h and down <= h and h > answer:
            answer = h
    return answer