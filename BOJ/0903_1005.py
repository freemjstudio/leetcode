# ACM Craft
# https://www.acmicpc.net/problem/1005

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    data = list(map(int, input().split())) # 건설에 걸리는 시간