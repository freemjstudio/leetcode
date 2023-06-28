# https://www.acmicpc.net/problem/17142

import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
array = []
answer = int(1e9) # 총 소요 시간
wall = 0 # 벽의 개수
virus_pos = [] # 2 번 좌표값

for i in range(n):
    data = list(map(int, input().split()))
    array.append(data)
    for j in range(n):
        if data[j] == 2:
            virus_pos.append([i, j])
        elif data[j] == 1:
            wall += 1

def bfs(v_list):
    visited = [[-1] * n for _ in range(n)]
    queue = deque([])
    for i in range(m):
        queue.append([v_list[i][0], v_list[i][1]])
        visited[v_list[i][0]][v_list[i][1]] += 1
    time = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1: # not visited
                if array[nx][ny] == 0: # 빈칸
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])
                    time = max(time, visited[nx][ny])
                elif array[nx][ny] == 2: # virus
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])

    # check
    check = 0
    for i in range(n):
        check += visited[i].count(-1)
    if check == wall:
        return time
    else:
        return int(1e9)

for comb in combinations(virus_pos, m):
    result = bfs(comb)
    answer = min(result, answer)

if answer == int(1e9):
    print(-1)
else:
    print(answer)