import collections
from typing import List

class Solution: # 스택구조를 활용한 풀이
    def isValid(self, s: str) -> bool:
        stack = []

        # 매핑 테이블을 만든다.
        table = {')': '(',
                 '}': '{',
                 ']': '['}

        # 열림기호는 스택에 push하고 닫힘기호는 스택에서 pop하여 매핑테이블과 비교한다.
        for char in s:
            if char not in table: # 열림기호라면
                stack.append(char)
            elif not stack or table[char] != stack.pop(): # 스택이 비어있거나 매핑된 테이블의 값과 다르다면
                return False
        return len(stack) == 0



answer = Solution()
print(answer.isValid(s = "()"))
print(answer.isValid(s = "()[]{}"))
print(answer.isValid(s = "(]"))
print(answer.isValid(s = "([)]"))
print(answer.isValid(s = "{[]}"))