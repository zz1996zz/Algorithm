import itertools


class Solution:
    def permute(self, nums):
        return list(map(list, itertools.permutations(nums)))


answer = Solution()
print(answer.permute(nums = [1,2,3]))
print(answer.permute(nums = [0,1]))
print(answer.permute(nums = [1]))

