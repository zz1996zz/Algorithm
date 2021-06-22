import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = collections.defaultdict(list)

        for word in strs:
            anagram[''.join(sorted(word))].append(word) # value 가 list 이기 때문에 list 메소드를 사용할 수 있다.

        return anagram.values()

answer = Solution()
print(answer.groupAnagrams(strs = ["eat", "tea", "tan", "ate", "nat", "bat"]))
print(answer.groupAnagrams(strs = [""]))
print(answer.groupAnagrams(strs = ["a"]))