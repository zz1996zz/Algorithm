import collections
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return nums.index(num), nums_map[target - num]


answer = Solution()
print(answer.twoSum(nums = [2,7,11,15], target = 9))
print(answer.twoSum(nums = [3,2,4], target = 6))
print(answer.twoSum(nums = [3,3], target = 6))