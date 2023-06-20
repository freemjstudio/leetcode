# https://school.programmers.co.kr/learn/courses/30/lessons/87694
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    board = [[0] * 50 for _ in range(50)]
    visited = [[0] * 50 for _ in range(50)]
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 2
                else:
                    board[i][j] = 1  # 테두리 그리기

    def bfs():
        queue = deque()
        queue.append([characterX, characterY])  # start
        visited[characterX][characterY] = 1  # 방문 표시
        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < 50 and 0 <= ny < 50 and board[nx][ny] == 1 and visited[nx][ny] == 0:  # 테두리인 경우에만 이동 가능
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])

    bfs()
    answer = visited[itemX][itemY]
    return answer