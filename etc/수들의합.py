import sys

sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
nlist = list(map(int, input().split()))
cnt = 0
nSum = 0
start, end = 0, 1

while start < N:
    nSum = sum(nlist[start:end])
    if nSum == M:
        cnt += 1
        start += 1
        if start == end:
            end += 1
    elif nSum < M and end < N+2:
        end += 1
    else:
        start += 1
        if start == end:
            end += 1

print(cnt)
