# https://school.programmers.co.kr/learn/courses/30/lessons/42861

def solution(n, costs):
    answer = int(1e9)  # min 값으로 갱신해 나가기
    graph = [[0] * n for _ in range(n)]

    for a, b, cost in costs:
        graph[a][b] = cost
        graph[b][a] = cost

        # 0 부터 가기

    def dfs(node, visited, total):
        nonlocal answer
        if sum(visited) == 4:
            # print(total)
            answer = min(answer, total)

        for x in range(n):
            if graph[node][x] != 0 and visited[x] == 0:
                visited[x] = 1
                dfs(x, visited, total + graph[node][x])
                visited[x] = 0

    for start in range(n):
        visited = [0] * n
        visited[start] = 1
        dfs(start, visited, 0)

    return answer