from collections import defaultdict
import sys
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
sum_dict = defaultdict(int)
for i in range(1, N+1):
    for j in range(1, M+1):
        sum_dict[i+j] += 1

klist = sorted(sum_dict.items(), key= lambda item: item[1], reverse=True)

x = klist[0][1]
for k, v in klist:
    if v != x:
        break
    print(k, end=" ")