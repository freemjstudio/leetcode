# https://leetcode.com/problems/climbing-stairs/?envType=study-plan-v2&envId=top-interview-150

'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

'''

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * 46
        dp[1] = 1
        dp[2] = 2

        if n >= 3:
            for i in range(3, 46):
                dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

