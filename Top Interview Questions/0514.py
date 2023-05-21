# https://leetcode.com/problems/longest-palindromic-substring/

# 역순으로 읽어도 같은 절
class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        n = len(s)

        for left in range(n):
            for right in range(left+1, n+1):
                temp = s[left:right]
                if temp == temp[::-1]:
                    if len(temp) > len(answer):
                        answer = temp
        if len(answer) == 0:
            return s[0]

        return answer
