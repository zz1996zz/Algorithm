import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
OX = list(map(int, input().split()))
cnt = 0
answer = 0

for i in OX:
    if i == 1:
        cnt += 1
        answer += cnt
    else:
        cnt = 0

print(answer)