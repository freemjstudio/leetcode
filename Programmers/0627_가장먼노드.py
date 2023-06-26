# https://school.programmers.co.kr/learn/courses/30/lessons/49189

import heapq

INF = int(1e9)


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]  # node 1 ~ n 까지
    distance = {node: INF for node in range(1, n + 1)}

    # graph 만들기
    for x, y in edge:
        graph[x].append[y]

    start = 1  # start node
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for next_dist, next in graph[node]:
            new_dist = next_dist + dist
            if new_dist < distance[next]:
                heapq.heappush(queue, [new_dist, next])

    m = max(distance)
    answer = distance.count(m)
    return answer