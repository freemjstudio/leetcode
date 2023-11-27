# https://www.acmicpc.net/problem/2133

N = int(input())
dp = [0] * (N+1)

if N%2 == 1: # 홀수
    print(0)
    exit(0)

dp[2] = 3

# dp 채우기
for i in range(4, 31, 2): # 짝수
    dp[i] = dp[i-2] * 3
    for j in range(0, i, 4):
        dp[i] += 2
        

print(dp[N])