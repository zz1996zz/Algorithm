import itertools


class Solution:
    def combine(self, n: int, k: int):
        return list(map(list, itertools.combinations(range(1,n+1), k)))


answer = Solution()
print(answer.combine(n = 4, k = 2))
print(answer.combine(n = 1, k = 1))

