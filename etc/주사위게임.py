import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
max_value = 0

for _ in range(N):
    nlist = list(map(int, input().split()))
    nlist.sort()
    temp = 0
    a, b, c = map(int, nlist)
    if a==b and a==c:
        temp = 10000 + a*1000
    elif a==c or b==c:
        temp = 1000 + c*100
    else:
        temp = c*100
    if max_value < temp:
        max_value = temp

print(max_value)