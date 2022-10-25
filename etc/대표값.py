import sys

sys.stdin = open("input.txt", "rt")

N = int(input())
nlist = list(map(int, input().split()))
average = round((sum(nlist) / N))
diff = 2143000000
max_value = 0
index = 0

for i in nlist:
    if diff >= abs(average - i):
        if diff > abs(average-i):
            diff = abs(average - i)
            max_value = i
            index = nlist.index(i) + 1
        if max_value < i:
            max_value = i
            index = nlist.index(i) + 1

print(average, index)
