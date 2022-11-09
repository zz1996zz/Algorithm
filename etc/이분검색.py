import sys

sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
nlist = list(map(int, input().split()))
nlist.sort()
lt, rt = 0, len(nlist) - 1

while lt <= rt:
    mid = (lt + rt) // 2
    if nlist[mid] == M:
        print(mid + 1)
        break
    elif nlist[mid] > M:
        rt = mid - 1
    else:
        lt = mid + 1
