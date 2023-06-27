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
empty = 0 # 빈칸 개수
wall = 0 # 벽의 개수
virus_pos = [] # 2 번 좌표값

for i in range(n):
    data = list(map(int, input().split()))
    array.append(data)
    empty += data.count(0)
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



for comb in combinations(virus_pos, m):
