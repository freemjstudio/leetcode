# https://www.acmicpc.net/problem/15683
N, M = map(int, input().split())
answer = N*M # 사각지대 최소크기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

array = []
for i in range(N):
    array.append(list(map(int, input().split())))

