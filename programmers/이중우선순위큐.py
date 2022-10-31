from collections import deque
from heapq import heapify, heappop, heappush


def solution(operations):
    answer = []
    data = []
    operations = deque(operations)

    while len(operations) != 0:
        n = operations.popleft()
        if 'I' in n:
            heappush(data, int(n[2:]))
        elif n == 'D 1' and len(data) != 0:
            data.sort()
            data.pop()
        elif n == 'D -1' and len(data) != 0:
            heapify(data)
            heappop(data)
    if len(data) == 0:
        answer = [0, 0]
    else:
        data.sort()
        x = data.pop()
        heapify(data)
        y = heappop(data)
        answer = [x, y]

    return answer

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))