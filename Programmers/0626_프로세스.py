# https://school.programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque([priorities])
    n = len(priorities)
    point = 0

    for i in range(n):
        if i < location:  # 왼쪽 앞에 있는 경우
            if priorities[i] >= priorities[location]:
                answer += 1
        elif i > location:
            if priorities[i] > priorities[location]:
                answer += 1
        else:
            # i == location
            continue

    return answer