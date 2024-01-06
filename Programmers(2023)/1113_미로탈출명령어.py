# https://school.programmers.co.kr/learn/courses/30/lessons/150365?language=python3
from collections import deque


def solution(n, m, x, y, r, c, k):
    INF = 'z' * (n * m)
    answer = INF
    board = [['.'] * m for _ in range(n)]
    x, y = x - 1, y - 1
    r, c = r - 1, c - 1
    board[x][y] = 'S'
    board[r][c] = 'E'
    # 좌 우 up down
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    literal = ['l', 'r', 'u', 'd']

    queue = deque([])
    queue.append([x, y, '', 0])
    while queue:
        x, y, route, step = queue.popleft()
        if board[x][y] == 'E' and step == k:
            if len(answer) > len(route):
                answer = route
            elif len(answer) == len(route):
                if answer > route:
                    answer = route
            print(route)
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                lit = literal[i]
                temp_route = route
                temp_step = step
                if 0 <= nx < n and 0 <= ny < m:
                    temp_route += lit
                    queue.append([nx, ny, temp_route, temp_step + 1])
    if answer == INF:
        return 'impossible'
    else:
        return answer 