import collections

# Counter를 이용한 계산 생략
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        count = 0

        for char in jewels:
            count += freqs[char]

        return count

answer = Solution()
print(answer.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(answer.numJewelsInStones(jewels = "z", stones = "ZZ"))

