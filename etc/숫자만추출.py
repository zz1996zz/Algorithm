import sys
sys.stdin = open("input.txt", "rt")

alpha = "abcdefghijklmnopqrstuvwxyz"
s = input()
answer = ''
cnt = 0

for i in s:
    if i in alpha or i in alpha.upper():
        continue
    else:
        answer += i
for i in range(1, int(answer) + 1):
    if int(answer) % i == 0:
        cnt += 1
print(int(answer))
print(cnt)