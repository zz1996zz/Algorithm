import sys

sys.stdin = open("input.txt", "rt")

N = int(input())
plate = [list(map(int, input().split())) for _ in range(N)]
max_value = -2147000000

# 행과 열의 합 구하기
for i in range(N):
    sum1 = sum2 = 0
    for j in range(N):
        sum1 += plate[i][j]
        sum2 += plate[j][i]
    if sum1 > max_value:
        max_value = sum1
    if sum2 > max_value:
        max_value = sum2
# 대각과 역대각 합 구하기
sum1=sum2=0
for i in range(N):
    sum1 += plate[i][i]
    sum2 += plate[i][-i-1]
if sum1 > max_value:
    max_value = sum1
if sum2 > max_value:
    max_value = sum2
print(max_value)