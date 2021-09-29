import collections
import heapq

# Counter를 이용한 음수 순 추출
class Solution:
    def topKFrequent(self, nums, k):
        freqs = collections.Counter(nums)
        freqs_heap = []

        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f)) # heapq는 키값이 작은 튜플을 0번째로 하기 때문에 음수로 넣는다(최소힙)

        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk

answer = Solution()
print(answer.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(answer.topKFrequent(nums = [1], k = 1))

