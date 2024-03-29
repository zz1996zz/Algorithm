import collections
import heapq


class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((v,w))

        Q = [(0, k)]

        dist = collections.defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v,w in graph[node]:
                    alt = time+w
                    heapq.heappush(Q, (alt, v))

        if len(dist) == n:
            return max(dist.values())
        return -1


answer = Solution()
print(answer.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
print(answer.networkDelayTime(times = [[1,2,1]], n = 2, k = 1))
print(answer.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))
