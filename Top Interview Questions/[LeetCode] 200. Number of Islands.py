# https://leetcode.com/problems/number-of-islands/?envType=study-plan-v2&envId=top-interview-150

'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

'''

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        N = len(grid)
        M = len(grid[0])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        answer = 0
        visited = [[False] * M for _ in range(N)]
        def bfs(x, y, visited):
            queue = deque([])
            queue.append((x, y))

            while queue:
                x, y = queue.popleft()
                visited[x][y] = True

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny] == '1':
                        visited[nx][ny] = True
                        queue.append(nx, ny)

        for i in range(N):
            for j in range(M):
                if grid[i][j] == "1" and not visited[i][j]: # 1 -> land
                    bfs(i, j, visited)
                    answer += 1
        return answer