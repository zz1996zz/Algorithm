import sys

sys.stdin = open("input.txt", "rt")

answer = []

for i in range(2):
    N = int(input())
    tmp = list(map(int, input().split()))
    for j in range(N):
        answer.append(tmp[j])

print(*(sorted(answer)))