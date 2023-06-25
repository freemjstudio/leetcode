# https://www.acmicpc.net/problem/2240
t, w = map(int, input().split())
dp = [[0] * (w+1) for _ in range(t+1)]
tree = [0] * (t+1)
# 자두 나무 정보 저장
for i in range(1, t+1):
    x = int(input())
    tree[i] = x

for i in range(t+1):
    # 0 회 움직이는 경우 채우기 dp[i][0]
    if (tree[i] == 1): # 1 번 나무
        dp[i][0] = dp[i-1][0] + 1
    else: # 2 번
        dp[i][0] = dp[i-1][0]

    # 1번 이상 움직이는 경우
    for j in range(1, w+1):
        if tree[i] == 1 and j%2 == 0: # 자두 나 1번 &  짝수번째 이동
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        elif tree[i] == 2 and j%2 == 1: # 자두 나무 2번 & 홀수번째 이동
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        else: # 이동 해도 자두 못 먹는 경우 !
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) # -1번 움직였을 때랑 -2 번 움직일 때 비교


# t 초 도달했을 때의 최대 값 출력
print(max(dp[t]))