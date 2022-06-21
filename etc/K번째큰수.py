# import sys
# sys.stdin = open("input.txt", "rt")
#
# N, K = map(int, sys.stdin.readline().split())
# nlist = sys.stdin.readline().split()
# result = []
#
# for x in range(len(nlist)):
#     for y in range(x+1, len(nlist)):
#         for z in range(y+1, len(nlist)):
#             sum = int(nlist[x]) + int(nlist[y]) + int(nlist[z])
#             if sum in result:
#                 continue
#             result.append(sum)
#
# result.sort(reverse=True)
# print(result[K-1])


import sys
sys.stdin = open("input.txt", "rt")

N, K = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))
result = set()

for x in range(N):
    for y in range(x+1, N):
        for z in range(y+1, N):
            result.add(nlist[x] + nlist[y] + nlist[z])
result = list(result)
result.sort(reverse=True)
print(result[K-1])