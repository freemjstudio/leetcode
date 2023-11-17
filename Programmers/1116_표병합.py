# https://school.programmers.co.kr/learn/courses/30/lessons/150366
from collections import defaultdict


def solution(commands):
    answer = []
    parents = [[(r, c) for r in range(51)] for c in range(51)]
    table = [["EMPTY"] * 51 for _ in range(51)]
    value_dict = defaultdict(list)

    # union-find 알고리즘
    def find_parents(r, c):
        if parents[r][c] == (r, c):
            return (r, c)
        p = parents[r][c]
        find_parents(p[0], p[1])

    def PRINT(r, c):
        return table[r][c]

    def UPDATE(r, c, value):
        table[r][c] = value

    def UPDATE2(value1, value2):
        # value1 을 가지고 있는 모든 셀 선택하기
        for i in range(1, 51):
            for j in range(1, 51):
                if table[i][j] == value1:
                    table[i][j] = value2

    def MERGE(r1, c1, r2, c2):
        if table[r1][c1] != "EMPTY":
            table[r2][c2] = table[r1][c1]
            parents[r2][c2] = (r1, c1)
        else:
            table[r1][c1] = table[r2][c2]
            parents[r1][c1] = (r2, c2)

    def UNMERGE(r, c):
        # parents 찾기
        p = find_parents(r, c)
        # parents 에 저장된 값
        original = table[p[0]][p[1]]

    for command in commands:
        cmd, *args = command.split()
        if cmd == "UPDATE":
            if len(args) == 3:
                r, c, value = args
                UPDATE(int(r), int(c), value)
            else:  # 2
                value1, value2 = args
                UPDATE2(value1, value2)
        elif cmd == "MERGE":
            r1, c1, r2, c2 = map(int, args)
            if r1 == r2 and c1 == c2:
                continue
            MERGE(r1, c1, r2, c2)
        elif cmd == "UNMERGE":
            r, c = map(int, args)
            UNMERGE(r, c)
        elif cmd == "PRINT":
            r, c = map(int, args)
            answer.append(PRINT(r, c))

    return answer