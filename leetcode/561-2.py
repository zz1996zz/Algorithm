import collections
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n

        return sum



answer = Solution()
print(answer.arrayPairSum(nums = [1,4,3,2]))
print(answer.arrayPairSum(nums = [6,2,6,5,1,2]))

