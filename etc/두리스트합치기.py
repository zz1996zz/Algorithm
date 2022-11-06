import sys

sys.stdin = open("input.txt", "rt")

N = int(input())
nlist = list(map(int, input().split()))
M = int(input())
mlist = list(map(int, input().split()))

nlist.extend(mlist)

print(*sorted(nlist))
