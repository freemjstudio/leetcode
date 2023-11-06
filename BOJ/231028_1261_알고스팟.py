# https://www.acmicpc.net/problem/1261
from collections import deque

N, M = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

board = [list(map(int, input())) for _ in range(N)]

queue = deque([])
queue.append([0, 0]) # x, y

# 벽 부신 횟수 저장하기
distance = [[-1] * M for _ in range(N)]
distance[0][0] = 0
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if distance[nx][ny] == -1: # 아직 방문하지 않은 칸 등장
                if board[nx][ny] == 0: # 통로
                    distance[nx][ny] = distance[x][y]
                    queue.append([nx, ny])
                else: # 벽
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append([nx, ny])

print(distance[N-1][M-1])