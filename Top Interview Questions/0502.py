# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Longest Substring without repeating characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 1  # maxLength
        # 반복되는 문자열 구하기
        n = len(s)
        for step in range(n, 0, -1):
            flag = False  # 중복된 문자열 나왔는지 체크하기
            check = ''  # 문자열
            for i in range(0, n, step):
                check = s[i:i + step]  # 확인할 문자열

        return answer