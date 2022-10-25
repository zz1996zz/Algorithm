from itertools import combinations
import sys
sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())
nlist = list(map(int, input().split()))
combi = list(combinations(nlist, 3))
temp = set()

for a, b, c in combi:
    temp.add(a+b+c)

temp = list(temp)
temp.sort(reverse=True)
print(temp[K - 1])