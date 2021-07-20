import collections
from typing import List


class Solution: # 스택을 활용한 풀이
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures) # 기본 디폴트 값은 0으로 해둔다.
        stack = [] # 인덱스가 담길 스택이다.

        for i, cur in enumerate(temperatures): # enumerate를 사용하여 인덱스와 값을 얻는다.
            # 현재 온도가 스택 값보다 높으면 인덱스 차이만큼을 answer스택에 저장한다.
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer


answer = Solution()
print(answer.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))
print(answer.dailyTemperatures(temperatures = [30,40,50,60]))
print(answer.dailyTemperatures(temperatures = [30,60,90]))