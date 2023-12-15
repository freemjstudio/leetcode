# https://leetcode.com/problems/word-search/?envType=study-plan-v2&envId=top-interview-150

from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        flag = True
        N = len(board)
        M = len(board[0])

        s = word[0] # initial alphabet

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def dfs(i, j, arr, idx):

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny <= M:
                    ch = board[nx][ny]

                    if word[idx] == arr[idx]:



        for i in range(N):
            for j in range(M):
                if board[i][j] == s:
                    # backtracking
                    dfs(i, j, [s], 1)


        return flag