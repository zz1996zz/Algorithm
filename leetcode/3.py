
# 슬라이딩 윈도우와 투 포인터로 사이즈 조절
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0

        for index, char in enumerate(s):
            if char in used and start <= used[char]: # 이미 등장한 문자라면 'start' 위치 갱신
                start = used[char] + 1
            else: # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)

            used[char] = index

        return max_length

answer = Solution()
print(answer.lengthOfLongestSubstring(s = "abcabcbb"))
print(answer.lengthOfLongestSubstring(s = "bbbbb"))
print(answer.lengthOfLongestSubstring(s = "pwwkew"))
print(answer.lengthOfLongestSubstring(s = ""))

