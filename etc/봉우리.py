import sys

sys.stdin = open("input.txt", "rt")

N = int(input())
plate = []
answer = 0
for _ in range(N+2):
    plate.append([0]*(N+2))
for i in range(N):
    tmp = list(map(int, input().split()))
    plate[i+1][1:N+1] = tmp

for i in range(1, N+1):
    for j in range(1, N+1):
        a = plate[i][j]
        if a>plate[i-1][j] and a>plate[i+1][j] and a>plate[i][j-1] and a>plate[i][j+1]:
            answer += 1
print(answer)