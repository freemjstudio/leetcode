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
check = [False] * m # customer 처리 완료

for j in range(m): # 승객 정보
    ax, ay, bx, by = map(int, input().split())
    customer.append([ax, ay, bx, by])

'''
1. 택시 위치에서 최단거리인 승객 뽑기 
2. 현재 연료양과 비교 -> -1 되면 exit하고 -1 출력 
3. -> 갈 수 있으면 연료 충전
'''

def bfs(sx, sy):
    visited = []
    queue = deque([])



if flag:
    print(answer)
else:
    print(-1)