import sys

sys.stdin = open("input.txt", "rt")


def row_valid(sdoku):
    global answer
    for i in range(9):
        tmp = sdoku[i]
        tmp = set(tmp)
        if len(tmp) != 9:
            answer = "NO"
            return


def col_valid(sdoku):
    global answer
    for i in range(9):
        tmp = list(zip(*sdoku))
        if len(tmp[i]) != 9:
            answer = "NO"
            return

def sdoku_valid(sdoku):
    global answer
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            valid=[]
            for k in range(3):
                tmp = sdoku[i + k][j:j + 3]
                valid.extend(tmp)
            valid = set(valid)
            if len(valid) != 9:
                answer = "NO"
                return

sdoku = [list(map(int, input().split())) for _ in range(9)]
answer = "YES"

row_valid(sdoku)
col_valid(sdoku)
sdoku_valid(sdoku)

print(answer)