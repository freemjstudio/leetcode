# ACM Craft -> 위상정렬
# https://www.acmicpc.net/problem/1005
from collections import deque

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    times = [0] + list(map(int, input().split())) # 건설에 걸리는 시간
    indegree = [0] * (n+1) # 진입차수. 나중에 0 이면 pop 할때라는 표시로 사용함
    graph = [[] for _ in range(n+1)] # 그래프 형태로 저장하기
    dp = [0] * (n+1) # i 번쨰 건물까지 걸린 time

    for _ in range(k):
        x, y = map(int, input().split()) # 건설 순서 x -> y
        graph[x].append(y)
        indegree[y] += 1 # 진입차수 1 증가

    w = int(input()) # 승리하기 위해 건설해야 하는 건물 (반드시 도착할 지점)
    queue = deque([])

    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i) # 진입 차수가 0 이면 queue 에 넣기
            dp[i] = times[i] # 초기 cost 저장하기
    while queue:
        now = queue.popleft()
        for next in graph[now]: # now -> 에서 갈 수 있는 node 탐색하기
            indegree[next] -= 1
            # dp 값 갱신하기
            dp[next] = max(dp[now] + times[next], dp[next]) # 누적되는 비용 갱신하기
            # 여기서 max 값을 저장해야 하는 이유는 모든 과정이 끝나야 next node로 갈 수 있기 때문이다 !
            if indegree[next] == 0:
                queue.append(next)

    # w 까지의 cost
    print(dp[w])