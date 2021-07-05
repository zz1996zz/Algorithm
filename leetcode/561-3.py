import collections
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])



answer = Solution()
print(answer.arrayPairSum(nums = [1,4,3,2]))
print(answer.arrayPairSum(nums = [6,2,6,5,1,2]))

