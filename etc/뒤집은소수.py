import sys
sys.stdin = open("input.txt", "rt")

def reverse(x:str):
    return int(''.join(list(reversed(x))))

def isPrime(x:int):
    if x == 1:
        return None
    for i in range(2, x):
        if x%i == 0:
            return None
    return x

N=int(sys.stdin.readline())
nums = list(map(str, sys.stdin.readline().split()))


for i in nums:
    num = reverse(i)
    if isPrime(num) != None:
        print(num, end=' ')