from heapq import heappop, heapify


def solution(jobs):
    answer, time, cnt = 0, 0, len(jobs)
    ready = []
    heapify(jobs)

    while len(jobs) != 0 or len(ready) != 0:
        while len(jobs) != 0:
            if time >= jobs[0][0]:
                n = heappop(jobs)
                ready.append([n[1], n[0]])
            else:
                break
        if len(ready) != 0:
            ready.sort(key=lambda x: x[0], reverse=True)
            m = ready.pop()
            answer += (time - m[1] + m[0])
            time += m[0]
        else: time += 1

    return answer // cnt