# https://school.programmers.co.kr/learn/courses/30/lessons/42860

def check():
    if name == start:
        return True
    return False


# A : 65, Z: 90
def solution(name):
    answer = 0
    n = len(name)
    start = n * 'A'
    name2num = []

    for i in range(n):
        name2num.append(ord(name[i]))
    print(name2num)

    pointer = 0
    while True:
        if check():
            break

        # 왼쪽 방향 오른쪽 방향 비교하기
        left_cnt, right_cnt = 0, 0

    return answer