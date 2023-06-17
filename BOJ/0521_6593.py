# https://www.acmicpc.net/problem/6593

from collections import deque

# 방향 이동 - 동서남북 + 상하
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append([sf, sx, sy]) # start point
    while queue:
        f, x, y = queue.pop()

        for i in range(6):
            nf, nx, ny = f + dz[i], x + dx[i], y + dy[i]
            if 0 <= nf < L and 0 <= nx < R and 0 <= ny < C and not visited[nf][nx][ny]:
                if building[nf][nx][ny] == "." or building[nf][nx][ny] == "E": # 통과할 수 있는 경우
                    dp[nf][nx][ny] = dp[f][x][y] + 1
                    visited[nf][nx][ny] = 1
                    queue.append([nf, nx, ny])


while True:
    L, R, C = map(int, input().split())
    if L == 0:
        break # test case end

    answer = 0 # 최소 시간
    dp = [[[0] * C for _ in range(R)] for _ in range(L)] # 최소 시간 정보 저장
    visited = [[[0] * C for _ in range(R)] for _ in range(L)] # 방문한 칸 기록
    building = [] # 전체 빌딩 정보

    # 출발점 & 탈출점
    sf, sx, sy = 0, 0, 0
    ef, ex, ey = 0, 0, 0

    for f in range(L):
        floor = [] # 이거 2차원 배열
        for i in range(R+1):
            data = input() # S....
            temp = [] # ['S', '.', '.', '.', '.']
            for j in range(len(data)):
                if data[j] == 'S':
                    sf, sx, sy = f, i, j
                if data[j] == 'E':
                    ef, ex, ey = f, i, j
                temp.append(data[j])

            if len(temp) == 0:
                continue
            floor.append(temp)
        building.append(floor)

    bfs()
    if dp[ef][ex][ey] != 0:

        print(f"Escaped in {dp[ef][ex][ey]} minute(s).")
    else:
        print("Trapped!")