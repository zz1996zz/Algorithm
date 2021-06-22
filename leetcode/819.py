import collections
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        nomal_strs = ''.join([word.lower() if word.isalnum() else ' ' for word in paragraph])
        words = [word for word in nomal_strs.split() if word not in banned]
        counts = collections.Counter(words)

        return counts.most_common(1)[0][0]


answer = Solution()
print(answer.mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
print(answer.mostCommonWord(paragraph = "a.", banned = []))

