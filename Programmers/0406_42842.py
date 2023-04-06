# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    pairs = []  # (col, row)
    total = brown + yellow
    col = 2
    row = total - col

    while col <= row:
        row = total - col
        if total % col == 0:
            pairs.append([col, total // col])
        col += 1

    for pair in pairs:
        c = pair[0]  # 직사각형 틀
        r = pair[1]

        for i in range(2, c + 1):  # col
            for j in range(2, r + 1):  # row
                if (c - i) * (r - j) == yellow:
                    return [r, c]

    return answer