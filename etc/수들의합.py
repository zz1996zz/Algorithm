import sys

sys.stdin = open("input.txt", "rt")

answer = 0
N, M = map(int, input().split())
nlist = list(map(int, input().split()))
i, j = 0, 1
while i < N:
    k = sum(nlist[i:j])
    if M == k:
        answer += 1
        i += 1
        if i == j:
            j += 1
    elif k < M and j < N+2:
        j += 1
    else:
        i += 1
        if i == j:
            j += 1

print(answer)