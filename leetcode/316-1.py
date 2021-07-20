import collections
from typing import List


class Solution: # 재귀를 이용한 분리
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]

            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char,''))
        return ''

answer = Solution()
print(answer.removeDuplicateLetters(s = "bcabc"))
print(answer.removeDuplicateLetters(s = "cbacdcbc"))