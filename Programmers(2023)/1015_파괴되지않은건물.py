# https://school.programmers.co.kr/learn/courses/30/lessons/92344

def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])

    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:  # 파괴
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    board[i][j] -= degree
        else:  # 회복
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    board[i][j] += degree

    # 파괴되지 않은 건물
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                answer += 1

    return answer