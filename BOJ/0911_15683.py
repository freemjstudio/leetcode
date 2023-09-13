import sys

N, M = map(int, input().split())
answer = N*M # 사각지대 최소크기

dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]

type = {1: [0, 1, 2, 3],
        2: [(0, 1), (2, 3)], # 상-하, 좌-우
        3: [(0,3), (1,3), (0, 2), (1, 2)],
        4: [(0,1,2), (0,1,3), (1,2,3), (0,2,3)],
        5: [(0,1,2,3)]} # 상하좌우

board = []
cctv = [] # [cctv_type, x, y]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    data = list(map(int, input().split()))
    for j in range(M):
        if 1 <= data[j] <= 5:
            cctv.append([data[j], i, j])
    board.append(data)

answer = N*M
# backtracking
def dfs(depth):
    global type, answer
    if depth == len(cctv):

        return

dfs(0)
print(answer)
