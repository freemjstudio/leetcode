# https://www.acmicpc.net/problem/6593

# 방향 이동 - 동서남북 , 상하
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():



while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break # 탈출
    flag = False
    answer = 0 # 최소 시간

    building = [] # 전체 빌딩 정보

    # 출발점 & 탈출점
    sf, sx, sy = 0, 0, 0
    ef, ex, ey = 0, 0, 0

    for f in range(L):
        floor = []
        for i in range(R):
            data = input()
            temp = []
            for j in data:
                if j == 'S':
                    sf, sx, sy = f, i, j
                if j == 'E':
                    ef, ex, ey = f, i, j

                floor.append(temp)
        building.append(floor)

    # bfs



    if flag:
        print(f"Escaped in {answer} minute(s).")
    else:
        print("Trapped!")

