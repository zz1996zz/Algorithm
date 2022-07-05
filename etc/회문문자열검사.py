import sys
sys.stdin = open("input.txt", "rt")

N = int(input())

for i in range(N):
    tmp = str(input()).upper()
    if tmp == tmp[::-1]:
        print("#{0} YES" .format(i+1))
    else:
        print("#{0} NO" .format(i+1))