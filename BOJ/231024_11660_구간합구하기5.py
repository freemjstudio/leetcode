# https://www.acmicpc.net/problem/11660

N, M = map(int, input().split())
board = []

def get_total(x1, y1, x2, y2):
    total = 0 # 총 누적합 구하기

    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            total += board[i][j]

    return total

for _ in range(N):
    board.append(list(map(int, input().split())))

# 미리 누적합 구해놓기
for i in range(N):
    for j in range(N):
        board[i][j] += board[i][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(get_total(x1-1, y1-1, x2-1, y2-1))