import sys

sys.stdin = open("input.txt", "rt")


def check_dvd(capacity):
    cnt = 1
    tmp = 0

    for v in music:
        diff = capacity - tmp
        if diff >= v:
            tmp += v
        else:
            cnt += 1
            tmp = v
    return cnt


N, M = map(int, input().split())
music = list(map(int, input().split()))
maxx = max(music)
lt, rt = 1, sum(music)
answer = 2147000000

while lt <= rt:
    capacity = (lt + rt) // 2
    cnt = check_dvd(capacity)

    if cnt <= M and capacity >= maxx:
        answer = capacity
        rt = capacity - 1
    else:
        lt = capacity + 1

print(answer)
