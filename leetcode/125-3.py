import collections

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = [c.lower() for c in s if c.isalnum()]
        return strs == strs[::-1]



answer = Solution()
print(answer.isPalindrome("A man, a plan, a canal: Panama"))
print(answer.isPalindrome("race a car"))

