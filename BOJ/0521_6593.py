from collections import deque

# 방향 이동 - 동서남북 + 상하
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append([sf, sy, sx]) # start point
    visited[sf][sy][sx] = 1
    while queue:
        f, y, x = queue.pop()

        for i in range(6):
            nf, ny, nx = f + dz[i], y + dy[i], x + dx[i]
            if 0 <= nf < L and 0 <= nx < C and 0 <= ny < R and not visited[nf][ny][nx]:
                if building[nf][ny][nx] == "." or building[nf][ny][nx] == "E": # 통과할 수 있는 경우
                    dp[nf][ny][nx] = dp[f][y][x] + 1
                    visited[nf][ny][nx] = 1
                    queue.append([nf, ny, nx])


while True:
    L, R, C = map(int, input().split())
    if L == 0:
        break # test case end

    dp = [[[0] * C for i in range(R)] for _ in range(L)] # 최소 시간 정보 저장
    visited = [[[0] * C for i in range(R)] for _ in range(L)] # 방문한 칸 기록
    building = [[] * R for i in range(L)] # 전체 빌딩 정보

    # 출발점 & 탈출점
    sf, sx, sy = 0, 0, 0
    ef, ex, ey = 0, 0, 0

    for i in range(L):
        for j in range(R):
            building[i].append(list(map(str, input())))
        input()
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == "S":
                    sf, sy, sx = i, j, k
                elif building[i][j][k] == "E":
                    ef, ey, ex = i, j, k
    bfs()

    if dp[ef][ey][ex] == 0:
        print("Trapped!")
    else:
        print("Escaped in %d minute(s)." % dp[ef][ey][ex])