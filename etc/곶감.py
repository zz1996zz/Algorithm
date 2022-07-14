import sys

sys.stdin = open("input.txt", "rt")

N = int(input())
plate = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
answer = 0

for i in range(M):
    row, direction, cnt = map(int, input().split())
    if direction==0:
        for _ in range(cnt):
            plate[row-1].append(plate[row-1].pop(0))
    else:
        for _ in range(cnt):
            plate[row-1].insert(0, plate[row-1].pop())

for i in range(N//2 + 1):
    if i != N//2:
        answer += sum(plate[i][i:N-i])
        answer += sum(plate[-i-1][i:N-i])
    else:
        answer += sum(plate[i][i:N-i])

print(answer)