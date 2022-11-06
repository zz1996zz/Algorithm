import sys

sys.stdin = open("input.txt", "rt")

cards = [i for i in range(1, 21)]

for _ in range(10):
    n, m = map(int, input().split())
    cards[n-1 : m] = reversed(cards[n-1:m])

print(*cards)