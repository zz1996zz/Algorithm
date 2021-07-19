import collections
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution: # 반복을 활용한 풀이
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            # 변수 b를 이용하여 swap해준다.
            b = head.next
            head.next = b.next
            b.next = head

            # 바뀌기 전 head의 전 노드인 prev를 이용하여 b를 가리키도록 한다.
            prev.next = b

            # 다음 비교를 위해 head는 다음 노드를, prev는 다다음 노드를 가리키게 한다.(페어스왑이므로)
            head = head.next
            prev = prev.next.next

        return root.next


answer = Solution()
print(answer.swapPairs(head = [1,2,3,4]))
print(answer.swapPairs(head = []))
print(answer.swapPairs(head = [1]))