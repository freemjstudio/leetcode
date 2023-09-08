# https://www.acmicpc.net/problem/19238
from collections import deque
n, m, fuel = map(int, input().split())
flag = False # -1
answer = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

array = []

for i in range(n): # n*n 배열
    data = list(map(int, input().split()))
    array.append(data)
sx, sy = map(int, input().split()) # 택시 출발 위치

customer = []

for j in range(m): # 승객 정보
    ax, ay, bx, by = map(int, input().split())
    customer.append([ax, ay, bx, by])

def bfs(sx, sy):
    queue = deque([])


if flag:
    print(answer)
else:
    print(-1)