import sys
sys.stdin = open("input.txt", "rt")

N = int(sys.stdin.readline())
nlist = [0] * (N + 1)
answer = 0

for i in range(2, N+1):
    if nlist[i] == 0:
        nlist[i] += 1
        answer += 1
        for j in range(i, N+1, i):
            nlist[j] += 1

print(answer)