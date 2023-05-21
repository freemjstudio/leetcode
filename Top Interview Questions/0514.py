# https://leetcode.com/problems/longest-palindromic-substring/

# 역순으로 읽어도 같은 절
class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        n = len(s)
        if n <= 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                answer = s
            else:
                answer = s[0]
        for left in range(n-1):
            for right in range(left+1, n):
                temp = s[left:right+1]
                if temp == temp[::-1]:
                    if len(temp) > len(answer):
                        answer = temp

        return answer
