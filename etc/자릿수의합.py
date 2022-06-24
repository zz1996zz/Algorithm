import sys
sys.stdin = open("input.txt", "rt")

def digit_sum(x):
    nSum = 0
    for i in x:
        nSum += int(i)
    return nSum

N = int(sys.stdin.readline())
nlist = list(map(str, sys.stdin.readline().split()))
max = -2147000000

for i in nlist:
    tmp = digit_sum(i)

    if tmp > max:
        answer = int(i)
        max = tmp
print(answer)