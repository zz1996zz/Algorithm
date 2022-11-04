import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
nlist = list(map(int, input().split()))
answer = 0
point = 0

for i in nlist:
    if i == 1:
        point += 1
        answer += point
    else:
        point = 0
print(answer)