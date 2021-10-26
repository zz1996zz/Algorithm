import collections
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)

        for u,v,w in flights:
            graph[u].append((v,w))

        Q=[(0, src, K)]

        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k>=0:
                for v,w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k-1))
        return -1


answer = Solution()
print(answer.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 1))
print(answer.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 0))
