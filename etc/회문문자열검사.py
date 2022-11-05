import sys
sys.stdin = open("input.txt", "rt")

N = int(input())

for i in range(N):
    s = input().lower()
    if s == ''.join(reversed(s)):
        print("#" + str(i+1) + " YES")
    else:
        print("#" + str(i+1) + " NO")