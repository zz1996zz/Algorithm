from itertools import permutations

def solution(numbers):
    answer = 0
    nset = set()
    for i in range(1, len(numbers) + 1):
        nset.update(map(int, map(''.join, permutations(numbers, i))))
    for i in nset:
        cnt = 0
        for j in range(2, i+1):
            if i % j == 0:
                cnt += 1
            if cnt > 1:
                break
        if cnt == 1:
            answer += 1
    return answer