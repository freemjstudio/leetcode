class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        N = len(matrix)
        M = len(matrix[0])

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        i, j = 0, 0
        visited = [[False] * M for _ in range(N)]
        k = 0 # direction

        for _ in range(N*M):
            answer.append(matrix[i][j])

            i, j = i + dx[k], j + dy[k]
            if not (0 <= i < N and 0 <= j < M) or visited[i][j]:
                i, j = i - dx[k], j - dy[k]
                k = (k+1) % 4

        return answer


# TEST CASE
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
s = Solution()
print(s.spiralOrder(matrix))

