# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Longest Substring without repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0  # maxLength
        # 반복되는 문자열 구하기
        n = len(s)
        for window in range(n, -1, -1):  #

        return answer