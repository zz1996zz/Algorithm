import sys

sys.stdin = open("input.txt", "rt")

K, N = map(int, input().split())
nlist = [int(input()) for _ in range(K)]
lt, rt = 1, max(nlist)

while lt <= rt:
    cnt = 0
    mid = (lt + rt) // 2
    for i in nlist:
        cnt += i // mid
    if cnt >= N:
        answer = mid
        lt = mid + 1
    else:
        rt = mid -1
print(answer)