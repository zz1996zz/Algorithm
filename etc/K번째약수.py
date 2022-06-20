N, K = map(int, input().split())
answer = 0

for i in range(1, N+1):
    if N%i == 0:
        answer+=1
    if answer == K:
        print(i)
        break
else:
    print(-1)