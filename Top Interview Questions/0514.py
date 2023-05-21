# https://leetcode.com/problems/longest-palindromic-substring/

# 역순으로 읽어도 같은 절
class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        n = len(s)
        for left in range(n-1):
            right = n-1
            temp = 0
            t_left = left
            t_right = right
            while left < right:
                if s[left] == s[right]:
                    temp += 2
                    left += 1
                    right -= 1
                else:
                    right -= 1
                    t_right = right

            if s[left] == s[right] and left == right:
                temp += 1
            if len(answer) < temp:
                answer = s[t_left:t_right+1]
        return answer



