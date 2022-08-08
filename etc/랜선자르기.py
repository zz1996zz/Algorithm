import sys

sys.stdin = open("input.txt", "rt")


def binary_search(lt, rt):
    global K, N, answer, lines
    cnt = 0
    medium = (lt + rt) // 2

    if lt <= rt:
        for line in lines:
            if line >= medium:
                cnt += line // medium
        if cnt >= N:
            answer = medium
            return binary_search(medium + 1, rt)
        else:
            return binary_search(lt, medium - 1)
    else:
        return


K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]
lines.sort()
answer = 0
lt, rt = 1, lines[-1]
binary_search(lt, rt)
print(answer)