import sys

sys.stdin = open("input.txt", "rt")

N = int(input())
board = [[i for i in list(map(int, input().split()))] for _ in range(N)]
answer, a, b = -2147000000, 0, 0
for i in range(N):
    tmp = 0
    for j in range(N):
        tmp += board[j][i]
    answer = max(answer, sum(board[i]), tmp)
for i in range(N):
    a += board[i][i]
    b += board[i][N-1-i]
answer = max(answer, a, b)

print(answer)