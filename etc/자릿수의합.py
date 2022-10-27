import sys

sys.stdin = open("input.txt", "rt")


def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum


N = int(input())
nlist = list(map(int, input().split()))
klist = list(digit_sum(x) for x in nlist)
max_num = 0;

max_num = max(klist)

print(nlist[klist.index(max_num)])
