# https://school.programmers.co.kr/learn/courses/30/lessons/150366
from collections import defaultdict

'''
["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", 
"MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", 
"PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
'''


def solution(commands):
    answer = []
    table = [[""] * 50 for _ in range(50)]
    value_dict = defaultdict(list)
    merged_dict = defaultdict(list)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 인접 하는 칸인지 체크하기
    def check(r1, c1, r2, c2):
        for i in range(4):
            nr = r1 + dx[i]
            nc = r1 + dy[i]
            if nr == r2 and nr == c2:
                return True
        return False

    for command in commands:
        x = command.split()
        if x[0] == "UPDATE":
            if len(x) == 4:
                r, c, value = int(x[1]) - 1, int(x[2]) - 1, x[3]
                table[r][c] = value
                value_dict[value].append((r, c))
            else:
                old_value, new_value = x[1], x[2]
                for r1, c1 in value_dict[old_value]:
                    table[r1][c1] = new_value
        elif x[0] == "MERGE":
            r1, c1, r2, c2 = int(x[1]) - 1, int(x[2]) - 1, int(x[3]) - 1, int(x[4]) - 1
            if r1 == r2 and c1 == c2:
                continue
                # 인접하는 경우
            if check(r1, c1, r2, c2):

            else:  # 인접하지 않는 경우



        elif x[0] == "UNMERGE":

        elif x[0] == "PRINT":
            r, c = int(x[1]) - 1, int(x[2]) - 1
            if table[r][c]:
                answer.append(table[r][c])
            else:
                answer.append("EMPTY")

    return answer