class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum(): # isalnum() 은 영문자, 숫자 여부를 판별하는 함수
                strs.append(char.lower())

        # 팰린드롬 여부 확인
        while len(strs)>1:
            if strs.pop(0) != strs.pop():
                return False

        return True



answer = Solution()
print(answer.isPalindrome("A man, a plan, a canal: Panama"))
print(answer.isPalindrome("race a car"))