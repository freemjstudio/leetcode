import sys
import copy
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
answer = int(1e9) # 사각지대 최소크기

dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]

c_type = {1: [[0], [1], [2], [3]],
        2: [(0, 1), (2, 3)], # 상-하, 좌-우
        3: [(0,3), (1,3), (0, 2), (1, 2)],
        4: [(0,1,2), (0,1,3), (1,2,3), (0,2,3)],
        5: [(0,1,2,3)]} # 상하좌우

board = []
cctv = [] # [cctv_type, x, y]
visited = [[False] * M for _ in range(N)]
total = 0

for i in range(N):
    data = list(map(int, input().split()))
    for j in range(M):
        if data[j] == 0:
            total += 1
        if 1 <= data[j] <= 5:
            cctv.append([data[j], i, j])
    board.append(data)

answer = N*M

# backtracking
def dfs(index, count):
    global c_type, answer, dx, dy, visited
    if index == len(cctv):
        if answer > (total-count) and (total-count) == 3:
            for v in visited:
                print(*v)
        answer = min(answer, total - count)
        return

    t, x, y = cctv[index]
    for i in range(len(c_type[t])): # 4개
        for j in range(len(c_type[t][i])):
            temp_visited = copy.deepcopy(visited)  # 변형하기 이전 형태 keep 하기
            temp_count = 0
            nx, ny = x, y

            while True:  # cctv 감시 칸 범위 벗어나기 이전까지 모두 확인
                nx += dx[c_type[t][i][j]]
                ny += dy[c_type[t][i][j]]
                if 0 <= nx < N and 0 <= ny < M:
                    if board[nx][ny] == 0 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        temp_count += 1
                    elif board[nx][ny] == 6:
                        break
                    else:  # cctv 자리
                        visited[nx][ny] = True
                else:
                    break
            dfs(index+1, count+temp_count)
            visited = temp_visited # 변형하기 이전으로 복귀하기

dfs(0, 0)
print(answer)
