import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
answer = 0
tmp = 0

for _ in range(N):
    nlist = list(map(int, input().split()))
    nlist.sort()
    a, b, c = map(int, nlist)
    if a==b and a==c:
        tmp = 10000 + (a*1000)
    elif a==b:
        tmp = 1000 + (a*100)
    elif b==c:
        tmp = 1000 + (b * 100)
    else:
        tmp = c * 100
    if tmp > answer:
        answer = tmp
print(answer)