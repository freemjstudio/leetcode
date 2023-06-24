# https://www.acmicpc.net/problem/2240
t, w = map(int, input().split())
dp = [[0] * (w+1) for _ in range(t+1)]
tree = [0] * (t+1)
# 자두 나무 정보 저장
for i in range(1, t+1):
    x = int(input())
    tree[i] = x

for i in range(t+1):



# t 초 도달했을 때의 최대 값 출력
print(max(dp[t]))