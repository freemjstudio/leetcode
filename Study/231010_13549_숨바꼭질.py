# https://www.acmicpc.net/problem/13549
INF = int(1e9)
MAX = 100001
N, K = map(int, input().split())

distance = [INF] * MAX

print(distance[K])
