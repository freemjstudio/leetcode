# https://leetcode.com/problems/coin-change/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount+1) # amount 에 도달하기 까지의 dp

        if dp[amount] != 0:
            return dp[amount]
        else:
            return -1 