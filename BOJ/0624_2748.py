# https://www.acmicpc.net/problem/2748 피보나치 수 2
n = int(input())

# 0 , 1, 1, 2, 3,
dp = [0] * (n+1)
dp[1] = 1
if n >= 2:
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
print(dp[n])