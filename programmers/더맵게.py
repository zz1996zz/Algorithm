from heapq import heapify, heappop, heappush

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while True:
        if len(scoville) < 2 and scoville[0] < K:
            answer = -1
            break
        l = heappop(scoville) + (2 * heappop(scoville))
        answer += 1
        heappush(scoville, l)
        if scoville[0] >= K:
            break

    return answer
