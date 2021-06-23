import collections
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            elem = target - n

            if elem in nums[i+1:]:
                return nums.index(n), nums[i+1:].index(elem)+(i+1)


answer = Solution()
print(answer.twoSum(nums = [2,7,11,15], target = 9))
print(answer.twoSum(nums = [3,2,4], target = 6))
print(answer.twoSum(nums = [3,3], target = 6))