import sys
sys.stdin = open("input.txt", "rt")

T = int(sys.stdin.readline())
for t in range(T):
    N, s, e, k = map(int, sys.stdin.readline().split())
    alist = list(map(int, sys.stdin.readline().split()))
    alist = sorted(alist[s-1:e])
    print("#{0} {1}" .format(t+1, alist[k-1]))