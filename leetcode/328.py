import collections
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution: # 반복구조를 활용한 풀이, 안의 값은 중요하지 않고 노드 그 자체가 홀수번째인지 짝수번째인지 확인하여 나열하는것이다.
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 예외를 처리해준다.
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        # 반복 구조로 홀수는 홀수끼리, 짝수는 짝수끼리 연결시킨다.
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # 홀수 마지막 노드를 짝수 첫번째 노드에 연결시킨다.
        odd.next = even_head

        return head



answer = Solution()
print(answer.oddEvenList(head = [1,2,3,4,5]))
print(answer.oddEvenList(head = [2,1,3,5,6,4,7]))