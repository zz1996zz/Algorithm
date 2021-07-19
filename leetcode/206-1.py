import collections
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution: # 재귀를 활용한 풀이, 연결리스트이므로 값을 가리킨다고 생각하지말고 주소를 가린킨다고 생각해
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node: # 연결리스트의 끝까지 다 오면 백트래킹하여 반환해준다.
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)



answer = Solution()
print(answer.reverseList(head = [1,2,3,4,5]))
print(answer.reverseList(head = [1,2]))