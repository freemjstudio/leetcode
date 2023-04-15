from collections import deque

n, m = map(int, input().split())
array = []

for i in range(n):
    data = list(map(int, input().split()))
    array.append(data)

biggest = 0 # 가장 큰 그림 사이즈
count = 0 # 그림 개수

visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    size = 1
    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = True
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and array[nx][ny] == 1:
                visited[nx][ny] = True
                size += 1
                queue.append((nx, ny))

    return size

for i in range(n):
    for j in range(m):
        if array[i][j] == 1 and not visited[i][j]:
            result = bfs(i, j)
            count += 1
            if result > 0:
                biggest = max(biggest, result)

print(count)
print(biggest)