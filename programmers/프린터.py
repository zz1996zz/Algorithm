from collections import deque
import heapq
def solution(priorities, location):
    answer = 0
    alpha = []
    heap = []
    # 우선순위 별 알파벳을 매칭시켜주었다.
    for i in range(len(priorities)):
        alpha.append(chr(65 + i))
    print(alpha)
    priorities = deque(zip(priorities, alpha))
    print(priorities)
    # 알파벳을 통해 해당 문서가 맞는지 확인한다.
    location = priorities[location][1]
    # 우선순위 큐를 사용하여 비교대상을 만듬
    heap = sorted(priorities, key=lambda x:x[0], reverse=True)
    print(heap)
    while len(priorities) != 0:
        n = priorities.popleft()
        if n[0] == heap[0][0]:
            answer += 1
            if n[1] == location:
                break
            heap.pop(0)
        else:
            priorities.append(n)
    return answer