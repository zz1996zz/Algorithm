import collections

# 가장 간단한 코드
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([s in jewels for s in stones])

answer = Solution()
print(answer.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(answer.numJewelsInStones(jewels = "z", stones = "ZZ"))

