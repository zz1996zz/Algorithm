import sys

sys.stdin = open("input.txt", "rt")

answer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for _ in range(10):
    start, end = map(int, input().split())
    tmp = answer[start-1:end]
    answer[start-1:end] = tmp[::-1]

print(*answer)