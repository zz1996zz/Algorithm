import sys

sys.stdin = open("input.txt", "rt")

T = int(input())
for i in range(1, T + 1):
    N, s, e, k = map(int, input().split())
    nlist = list(map(int, input().split()))
    klist = nlist[s - 1:e]
    klist.sort()
    print("#{0} {1}".format(i, klist[k - 1]))