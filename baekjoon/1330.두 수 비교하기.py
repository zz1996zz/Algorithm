class Solution:
    def answer_function(self, num1, num2):
        if num1 > num2:
            return '>'
        elif num1 < num2:
            return '<'
        else:
            return '=='

answer = Solution()
print(answer.answer_function(1, 2))
print(answer.answer_function(10, 2))
print(answer.answer_function(5, 5))