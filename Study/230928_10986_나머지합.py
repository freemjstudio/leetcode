# https://www.acmicpc.net/problem/10986
N, M = map(int, input().split())
data = list(map(int, input().split()))
answer = 0
dp = [[0] * (N+1) for _ in range(N+1)] # 누적합 저장 dp[i][j] 는 i ~ j 까지의 합

# 누적합 저장하기
for i in range(N):
    for j in range(i, N):
        if i == j:
            dp[i][j] = data[i]
        else:
            dp[i][j] = dp[i][j-1] + data[j]

# 누적합을 M 으로 나누기

print(answer)