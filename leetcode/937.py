import collections
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits= [], []
        for log in logs:
            if log.split()[1].isdigit(): # isdigit() 는 문자열이 숫자로만 이루어져 있는지 알려주는 함수. 음수나 소수점이 있으면 False를 반환.
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits



answer = Solution()
print(answer.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
print(answer.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))

