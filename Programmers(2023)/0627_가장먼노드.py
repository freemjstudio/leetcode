# https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque
def solution(n, edge):

    answer = 0
    graph = [[] for _ in range(n + 1)]  # node 1 ~ n 까지
    distance = [-1] * (n + 1)  # 방문 x == -1, 거리 저장

    # graph 만들기
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    # bfs
    start = 1  # start node
    queue = deque([])
    queue.append(start)
    distance[start] = 0  # 출발 노드이므로 거리 0

    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if distance[next] == -1:
                queue.append(next)
                distance[next] = distance[now] + 1

    m = max(distance)
    for d in distance:
        if d == m:
            answer += 1
    return answer