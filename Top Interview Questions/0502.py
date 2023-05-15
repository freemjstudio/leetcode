# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Longest Substring without repeating characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0 # maxLength

        # 반복되는 문자열 구하기
        n = len(s)

        for left in range(n-1):
            temp_set = set()
            temp_set.add(s[left])
            for right in range(left+1, n):
                if s[right] not in temp_set:
                    temp_set.add(s[right])
                else:
                    break
            answer = max(len(temp_set), answer)

        return answer