import sys
sys.stdin = open("input.txt", "rt")

tmp = input()
answer = ""
cnt = 0
alpha = "abcdefghijklmnopqrstuvwxyz"

for i in tmp:
    i = i.lower()
    if i not in alpha:
        answer += i

for i in range(1, int(answer)+1):
    if int(answer)%i == 0:
        cnt += 1

print(int(answer))
print(cnt)