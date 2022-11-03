import sys

sys.stdin = open("input.txt", "rt")


def reverse(x):
    return int(''.join(list(reversed(str(x)))))


def isPrime(x):
    cnt = 0
    temp = True
    for i in range(1, x + 1):
       if x % i == 0:
           cnt += 1
       if cnt > 2:
           temp = False
           break
    return temp

N = int(input())
nlist = list(map(int, input().split()))

for i in range(N):
    reverse_num = reverse(str(nlist[i]))
    if reverse_num != 1 and isPrime(reverse_num):
        print(reverse_num, end=" ")
