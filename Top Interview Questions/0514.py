# https://leetcode.com/problems/longest-palindromic-substring/

# 역순으로 읽어도 같은 절
class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = 1
        n = len(s)
        for left in range(n-1):
            right = n-1
            temp = 0
            while left < right:
                if s[left] == s[right]:
                    temp += 2
                    left += 1
                    right -= 1

            if s[left] == s[right]:
                temp += 1
            answer = max(temp, answer)



