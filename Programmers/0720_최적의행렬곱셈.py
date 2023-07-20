# 최적의 행렬 곱셈


def solution(matrix_sizes):
    answer = 0
    n = len(matrix_sizes)
    INF = int(1e9)
    dp = [[INF] * n for _ in range(n)]

    return answer