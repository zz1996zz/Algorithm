import collections

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = collections.deque()
        for c in s:
            if c.isalnum():
                strs.append(c.lower())
        while len(strs)>1:
            if strs.popleft() != strs.pop():
                return False
        return True



answer = Solution()
print(answer.isPalindrome("A man, a plan, a canal: Panama"))
print(answer.isPalindrome("race a car"))

