# https://school.programmers.co.kr/learn/courses/30/lessons/92344
def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])

    for t, r1, c1, r2, c2 in skill:
        if t == 1:  # 파괴

        else:  # 회복

    # 파괴되지 않은 건물
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                answer += 1

    return answer