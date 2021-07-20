import collections
from typing import List


class Solution: # 스택을 이용한 문자 제거
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1

            if char in seen: # 스택에 포함되어 있는거면 continue 시킨다.
                continue

            while stack and char < stack[-1] and counter[stack[-1]] > 0: # 스택이 비어있지 않고, char이 stack의 top보다 값이 크고, 개수가 더 남아있다면 stack과 seen에서 삭제한다.
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return ''.join(stack)

answer = Solution()
print(answer.removeDuplicateLetters(s = "bcabc"))
print(answer.removeDuplicateLetters(s = "cbacdcbc"))