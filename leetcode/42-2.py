import collections
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break

                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                volume += distance * waters
            stack.append(i)
        return volume


answer = Solution()
print(answer.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
print(answer.trap(height = [4,2,0,3,2,5]))