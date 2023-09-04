# ACM Craft
# https://www.acmicpc.net/problem/1005

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    time = list(map(int, input().split())) # 건설에 걸리는 시간
    for _ in range(k):
        x, y = map(int, input().split()) # 건설 순서 x -> y
    w = int(input()) # 승리하기 위해 건설해야 하는 건물 (반드시 도착할 지점)

