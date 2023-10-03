# https://www.acmicpc.net/problem/15591
from collections import deque

N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
for _ in range(N-1): # edge 정보
    p, q, r = map(int, input().split())
    graph[p].append([q, r])

def solve(K, V):
    result = 0 # K 이상인 영상 개수
    usado = [INF] * (N+1) # distance 대신 저장하기
    visited = [False] * (N+1)

    queue = deque([V])
    visited[V] = True
    usado[V] = 0
    while queue:
        now = queue.popleft()
        for next, r in graph[now]:
            if not visited[next]:
                visited[next] = True
                usado[next] = min(usado[next], r)
                queue.append(next)

    for i in range(1, N+1):
        if i == V:
            continue
        elif usado[i] >= K:
            result += 1
    return result

# v 와 유사도가 K 이상인 동영상 개수 구하기
for _ in range(Q):
    k, v = map(int, input().split())
    print(solve(k, v))