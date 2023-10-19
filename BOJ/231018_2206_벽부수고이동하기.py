# https://www.acmicpc.net/problem/2206
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    queue = deque([sx, sy, True])
    visited = [[-1] * M for _ in range(N)] # -1 이면 not visited , 0 이상은 distance 값 저장
    visited[sx][sy] = 0
    while queue:
        x, y, flag = queue.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and board[nx][ny] == 0: # 이동 가능한 경우
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny, flag]) # flag 는 동일하게 주기
                elif not visited[nx][ny] and board[nx][ny] == 0: # 벽을 만난 경우
                    if flag:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append([nx, ny, False])
    return -1

print(bfs(0, 0))
