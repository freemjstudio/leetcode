# https://leetcode.com/problems/word-search/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        global flag
        N = len(board)
        M = len(board[0])
        visited = [[False] * M for _ in range(N)]
        s = word[0] # initial alphabet

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def dfs(x, y, arr, idx, visited):
            global flag
            nw = "".join(arr)
            if len(nw) == len(word):
                flag = True
                return
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    ch = board[nx][ny]

                    if word[idx] == ch:
                        arr.append(ch)
                        visited[nx][ny] = True
                        dfs(nx, ny, arr, idx+1, visited)
                        visited[nx][ny] = False
                        arr.pop()

        flag = False
        for i in range(N):
            for j in range(M):
                if board[i][j] == s and not visited[i][j]:
                    visited[i][j] = True
                    dfs(i, j, [s], 1, visited)
                    visited[i][j] = False

        return flag