import collections
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution: # 값만 교환하는 변칙적인 풀이
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head


answer = Solution()
print(answer.swapPairs(head = [1,2,3,4]))
print(answer.swapPairs(head = []))
print(answer.swapPairs(head = [1]))