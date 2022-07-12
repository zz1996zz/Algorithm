import sys

sys.stdin = open("input.txt", "rt")

N = int(input())
plate = [list(map(int, input().split())) for _ in range(N)]
answer = 0
for i in range(N // 2 + 1):
    if i < N // 2:
        answer += sum(plate[i][N // 2 - i:N // 2 + i + 1])
        answer += sum(plate[-i - 1][N // 2 - i:N // 2 + i + 1])
    else:
        answer += sum(plate[i][0:N])

print(answer)