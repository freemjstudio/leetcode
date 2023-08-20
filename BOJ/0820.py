# https://www.acmicpc.net/problem/2304
N = int(input()) # 기둥 개수
answer = 0
bars = []
for _ in range(N):
    L, H = map(int, input().split())
    bars.append([L, H])

bars.sort() # [[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]
print(answer)
