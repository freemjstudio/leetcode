# https://school.programmers.co.kr/learn/courses/30/lessons/87694

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(cx, cy):
    queue = deque()
    queue.append([cx, cy])  # start
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 50 and 0 <= ny < 50 and board[nx][ny] == 1:  # 테두리인 경우에만 이동 가능
                board[nx][ny] = board[x][y] + 1
                queue.append([nx, ny])


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    board = [[0] * 50 for _ in range(50)]

    for x1, y1, x2, y2 in rectangle:
        for

    answer = board[itemX][itemY]
    return answer