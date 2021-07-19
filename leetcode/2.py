import collections
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution: # 가산기를 활용한 풀이
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0 # 덧셈을 하였을때 자릿수가 넘어가는 것을 저장해주는 변수
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l1 = l1.next

            carry, val = divmod(sum+carry, 10) # 아래자리에서 올라온 값을 더해서 10으로 나눠서 몫과 나머지를 구해준다.

            head.next = ListNode(val) # 나머지 값을 노드로 만들어서 연결리스트로 만들어준다.
            head = head.next

        return root.next


answer = Solution()
print(answer.addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))
print(answer.addTwoNumbers(l1 = [0], l2 = [0]))