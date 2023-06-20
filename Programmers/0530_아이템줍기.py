from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    board = [[-1] * 102 for _ in range(102)]
    visited = [[0] * 102 for _ in range(102)]
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, rec)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 0
                elif board[i][j] != 0:  # 이미 직사각형 안이 아니면서, 테두리로 그릴 수 있는 경우 -> 직사각형끼리 겹치는 경우 방지
                    board[i][j] = 1  # 테두리 그리기

    def bfs():
        queue = deque()
        queue.append([characterX * 2, characterY * 2])  # start
        visited[characterX * 2][characterY * 2] = 1  # 방문 표시
        while queue:
            x, y = queue.popleft()
            if x == itemX * 2 and y == itemY * 2:
                answer = (visited[x][y] - 1) // 2
                return answer
                break
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if board[nx][ny] == 1 and visited[nx][ny] == 0:  # 테두리인 경우에만 이동 가능
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])

    answer = bfs()

    return answer