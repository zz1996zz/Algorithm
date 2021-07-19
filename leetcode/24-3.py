import collections
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution: # 재귀 구조로 스왑
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head



answer = Solution()
print(answer.swapPairs(head = [1,2,3,4]))
print(answer.swapPairs(head = []))
print(answer.swapPairs(head = [1]))