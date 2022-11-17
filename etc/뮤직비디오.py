import sys

sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
musics = list(map(int, input().split()))

lt = 0
rt = 10000 * M + 1
answer = 2147000000

while lt <= rt:
    medium = (lt + rt) // 2
    cnt = 1
    nSum = 0

    for i in musics:
        if medium < nSum + i:
            cnt += 1
            if medium == nSum + i:
                nSum = 0
            nSum = i
        else: nSum += i

    if cnt <= M:
        answer = min(answer, medium)
        rt = medium - 1
    elif cnt > M:
        lt = medium + 1

print(answer)
