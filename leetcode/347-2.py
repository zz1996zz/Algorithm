import collections
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        return list(zip(*collections.Counter(nums).most_common(k)))[0]

answer = Solution()
print(answer.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(answer.topKFrequent(nums = [1], k = 1))

