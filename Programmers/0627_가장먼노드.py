# https://school.programmers.co.kr/learn/courses/30/lessons/49189
INF = int(1e9)


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]  # node 1 ~ n 까지
    distance = [INF] * (n + 1)

    return answer