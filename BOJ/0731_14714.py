# https://www.acmicpc.net/problem/14714
from collections import deque

n, a, b, da, db = map(int, input().split())
a -= 1
b -= 1 # index 맞추기
flag = False

# #  visited[a or b][a누구][b누구]
#
visited = [[[0] * 2 for _ in range(n)] for _ in range(n)] # 3차원 배열
visited[0][a][b] = 1 # 0 == a 지목권
visited[1][a][b] = 1 # 1 == b 지목권
queue = deque([(a, b, 1)]) # 현재 지목권 가진 사람 a, b, 지목 횟수

while queue:
    cur_a, cur_b, count = queue.popleft()
    if count % 2 == 1: # A
    else: # B

INF = int(1e9)
answer = INF
# min 값 찾기
for i in range(n):
    if visited[0][i][i] != 0 and visited[0][i][i] < answer:
        answer = visited[0][i][i]
    if visited[1][i][i] != 0 and visited[1][i][i] < answer:
        answer = visited[1][i][i]

if answer == INF:
    print("Evil Galazy")
else:
    print(answer-1)