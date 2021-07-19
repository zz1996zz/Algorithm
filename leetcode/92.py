import collections
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution: # 반복구조를 활용한 풀이
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 예외처리
        if not head or left == right:
            return head

        root = start = ListNode(None)
        root.next = head

        # start와 end 지정
        for _ in range(left - 1):
            start = start.next
        end = start.next

        # 반복하면서 노드를 차례대로 뒤집는다.
        for _ in range(right - left):
            temp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = temp

        return root.next




answer = Solution()
print(answer.reverseBetween(head = [1,2,3,4,5], left = 2, right = 4))
print(answer.reverseBetween(head = [5], left = 1, right = 1))