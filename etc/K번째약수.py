import sys
sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())
nlist = [x for x in range(1, N+1) if N % x == 0]
if K > len(nlist):
    print(-1)
else:
    print(nlist[K - 1])