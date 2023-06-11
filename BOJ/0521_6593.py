# https://www.acmicpc.net/problem/6593

from collections import deque

# 방향 이동 - 동서남북 , 상하
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(building, sf, sx, sy, ef, ex, ey, L, C, R):
    time = 0  #
    queue = deque([])
    queue.append((sf, sx, sy)) # start point
    while queue:

        f, x, y = queue.pop()
        if building[x][x][y] == 'E':
            return time

        if f == ef:  # 목적지 층에 도착 ,
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and building[f][nx][ny] != '#':
                    queue.append((f, nx, ny))

        else:  # 시작층, 목적지층 아닌 경우
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and building[f][nx][ny] != '#':
                    queue.append((f, nx, ny))
            # 상층 이동
            nf = f + 1
            if nf < L and building[nf][x][y] != '#':
                queue.append((nf, x, y))

    return 0

while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break # test case end

    answer = 0 # 최소 시간
    building = [] # 전체 빌딩 정보

    # 출발점 & 탈출점
    sf, sx, sy = 0, 0, 0
    ef, ex, ey = 0, 0, 0

    for f in range(L):
        floor = [] # 이거 2차원 배열로 만들어야 함
        for i in range(R):
            data = input()
            temp = []
            for j in data:
                if j == 'S':
                    sf, sx, sy = f, i, j
                if j == 'E':
                    ef, ex, ey = f, i, j
                temp.append(j)
            floor.append(temp)
        building.append(floor)
    print(building)

    answer = bfs(building, sf, sx, sy, ef, ex, ey, L, C, R)
    if answer:
        print(f"Escaped in {answer} minute(s).")
    else:
        print("Trapped!")

