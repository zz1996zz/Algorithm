import collections
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution: # 연결리스트에 있는 값들을 리스트로 옮겨서 푸는 방식
    def isPalindrome(self, head: ListNode) -> bool:
        q = []
        if not head: # 연결리스트가 비어있을 때
            return False

        node = head
        while node is not None: # 연결리스트에 있는 값들을 리스트로 옮긴다
            q.append(node.val)
            node = node.next

        while len(q) > 1: # 리스트의 처음과 끝을 비교해서 팰린드롬이면 True를 아니면 False를 반환
            if q.pop(0) != q.pop():
                return False

        return True




answer = Solution()
print(answer.isPalindrome(head = [1,2,2,1]))
print(answer.isPalindrome(head = [1,2]))