import sys

sys.stdin = open("input.txt", "rt")

N = int(input())
nlist = [0] * (N + 1)
answer = 0

for i in range(2, N + 1):
    if nlist[i] == 0:
        answer += 1
        nlist[i] += 1
        for j in range(i, N + 1, i):
            nlist[j] += 1
print(answer)
