# https://www.acmicpc.net/problem/1261
from collections import deque

N, M = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

board = []
answer = N*M

for _ in range(N):
    data = list(input())
    board.append(data)

queue = deque([])
queue.append([0, 0]) # x, y

# 벽 부신 횟수 저장하기
distance = [[-1] * M for _ in range(N)]
distance[0][0] = 0
while queue:
    x, y = queue.popleft()

    if x == N-1 and y == M-1: # 도착점
        answer = min(answer, distance[x][y])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == '1':
                if distance[nx][ny] == -1: # 방문 처리 안된 경우
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append([nx, ny])
            else: # board[nx][ny] == '0'
                if distance[nx][ny] == -1:
                    distance[nx][ny] += 1
                    queue.append([nx, ny])


print(answer)