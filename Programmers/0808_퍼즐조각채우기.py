# https://school.programmers.co.kr/learn/courses/30/lessons/84021
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_position(sx, sy, table, visited, mode = 1):
    one_piece = [(sx, sy)] # 한 조각을 이루는 좌표 리스트
    visited[sx][sy] = True
    queue = deque(one_piece)
    n = len(table)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and table[nx][ny] == mode:
                visited[nx][ny] = True
                queue.append((nx, ny))
                one_piece.append((nx, ny))

    return one_piece

def rotate_puzzle(one_piece): # ex. [(0,0), (1,0)]
    # 90 도 회전한 퍼즐 모양 모음
    rotated_puzzle_list = [one_piece]

    for i in range(3):
        new_pos = []
        for x, y in one_piece[-1]:
            nx = -y
            ny = x
            new_pos.append((nx, ny))
        rotated_puzzle_list.append(new_pos)

    return rotated_puzzle_list

# table 2차원 배열에서 퍼즐 조각의 위치 & 모양 저장하기 -> dfs
def get_puzzle(table):
    puzzle_list = [] # [cnt, (x1,y1), (x2,y2)] , [cnt, (a1, b1), .. ] ...
    n = len(table)
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if table[i][j] and not visited[i][j]:
                one_piece = get_position(i, j, table, visited, 1)
                count = len(one_piece)
                # rotate 시킨 좌표까지

                puzzle_list.append([count]+rotate_puzzle(one_piece))
    return puzzle_list

def check(game_board, puzzle, x, y):
    n = len(game_board)
    for px, py in puzzle:    # puzzle 안에 있는 모든 좌표들이 조건에 맞아야 함
        nx, ny = x + px, y + py
        if 0 <= nx < n and 0 <= ny < n and game_board[nx][ny] == 0:
            continue
        else:
            return False
    return True


# 0 인 칸을 찾아야 함 !
def dfs(puzzle_list, game_board):

    answer = 0
    n = len(game_board)
    m = len(puzzle_list)
    visited = [[False] * n for _ in range(n)]
    check_puzzle = [False] * m

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and game_board[i][j] == 0:
                one_vacant = get_position(i, j, game_board, 0) # 빈칸 크기
                size_vacant = len(one_vacant)

                # puzzle_list에 빈공간에 들어갈 수 있는 조각 확인
                for vx, vy in one_vacant:
                    flag = False
                    # puzzle_list
                    for k in range(m):
                        if check_puzzle[k]: # 이미 사용한 퍼즐 조각
                            continue
                        size_puzzle = puzzle_list[k][0]
                        if size_puzzle != size_vacant: # 반드시 크기가 딱 맞아야 함 !
                            continue
                        for puzzle in puzzle_list[k][1:]:
                            if check(game_board, puzzle, vx, vy): # true
                                flag = True
                                answer += size_puzzle
                                break
                        if flag:
                            break
                    if flag:  # 이미 처리된 경우에 for 문을 탈출시키고 다음 vacant 확인하기 !
                        break
    return answer




def solution(game_board, table):
    puzzle_list = get_puzzle(table)
    answer = dfs(puzzle_list, game_board)

    return answer