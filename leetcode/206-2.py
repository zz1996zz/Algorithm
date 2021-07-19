import collections
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution: # 반복을 이용한 풀이
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev


answer = Solution()
print(answer.reverseList(head = [1,2,3,4,5]))
print(answer.reverseList(head = [1,2]))