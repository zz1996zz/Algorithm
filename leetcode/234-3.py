import collections
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution: # 런너기법을 활용한 풀이
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        rev = None

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast: # 입력값의 개수가 홀수일때, 중간값을 빗겨나가게 해준다.
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev # rev가 비어있으면 참, rev가 안비어있으면 거짓



answer = Solution()
print(answer.isPalindrome(head = [1,2,2,1]))
print(answer.isPalindrome(head = [1,2]))