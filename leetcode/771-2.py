import collections

# defaultdict를 이용한 비교 생략
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        # if문으로 비교없이 빈도 수를 계산하여 코드 수를 줄일 수 있다.
        for char in stones:
            freqs[char] += 1

        for char in jewels:
            count += freqs[char]

        return count

answer = Solution()
print(answer.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(answer.numJewelsInStones(jewels = "z", stones = "ZZ"))

