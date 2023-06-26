# https://school.programmers.co.kr/learn/courses/30/lessons/49189

def solution(n, edge):
    INF = int(1e9)

    answer = 0
    graph = [[] for _ in range(n + 1)]  # node 1 ~ n 까지
    distance = [0] * (n + 1)

    # # graph 만들기
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    m = max(distance)
    for d in distance:
        if d == m:
            answer += 1
    return answer