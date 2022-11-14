def solution(number, k):
    answer = ''
    nlist = [x for x in number]
    nlist.sort()
    nlist = nlist[:len(number) - k]
    n = 0
    for i in number:
        if i not in nlist or n== k:
            answer += i
        else:
            n += 1
    return answer

print(solution("1924", 2))
