# https://leetcode.com/problems/longest-palindromic-substring/

# 역순으로 읽어도 같은 절
class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        n = len(s)
        if n <= 1:
            return s
        for left in range(n):
            right = n - 1
            temp = 0
            t_left = left
            t_right = right
            while left < right:
                if s[left] == s[right]:
                    temp += 2
                    left += 1
                    right -= 1
                else:
                    left = t_left
                    right -= 1
                    temp = 0
                    t_right = right

            if len(answer) < temp:
                answer = s[t_left:t_right + 1]

        if len(s) == 2:
            if s[0] == s[1]:
                answer = s
            else:
                answer = s[0]
        return answer
