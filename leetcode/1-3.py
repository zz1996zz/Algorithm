import collections
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]


answer = Solution()
print(answer.twoSum(nums = [2,7,11,15], target = 9))
print(answer.twoSum(nums = [3,2,4], target = 6))
print(answer.twoSum(nums = [3,3], target = 6))