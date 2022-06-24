from collections import Counter
import sys
sys.stdin = open("input.txt", "rt")

N, M = map(int, sys.stdin.readline().split())
answer = []
max = 0

sum_value = [x+y for x in range(1, N+1) for y in range(1, M+1)]
sum_value = dict(Counter(sum_value))
nlist = list(sum_value.items())

for key, value in nlist:
    if len(answer) == 0:
        answer.append(key)
        max = value
    elif value > max:
        answer.clear()
        answer.append(key)
        max = value
    elif value == max:
        answer.append(key)

print(*answer)