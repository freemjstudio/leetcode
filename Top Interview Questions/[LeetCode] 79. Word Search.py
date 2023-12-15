# https://leetcode.com/problems/word-search/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        flag = True
        N = len(board)
        M = len(board[0])

        s = word[0]

        for i in range(N):
            for j in range(M):
                if board[i][j] == s:
                    # backtracking


        return flag