
# 해시테이블을 이용한 풀이
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}
        count = 0

        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        for char in jewels:
            if char in freqs:
                count += freqs[char]

        return count

answer = Solution()
print(answer.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(answer.numJewelsInStones(jewels = "z", stones = "ZZ"))

