# https://leetcode.com/problems/factorial-trailing-zeroes/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def trailingZeroes(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(n+1):
            dp[i] = dp[i//5] + i//5

        return dp[n]