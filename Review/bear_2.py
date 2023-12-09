def check(board):  # check tic tac toe
    for i in range(3):  # 세로
        if board[i][0] == board[i][1] == board[i][2] != '-':
            return True  # 가로
        if board[0][i] == board[1][i] == board[2][i] != '-':
            return True
            # 대각선 좌상-우하
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return True
        # 대각선 우상-좌하
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return True
    return False


def GameChallenge(strArr):
    idx = 3
    board = [[""] * 3 for _ in range(3)]
    newStr = []
    for i in strArr:
        if i != "<>":
            newStr.append(i)

    for i in range(9):
        board[i // 3][i % 3] = newStr[i]

    idx_dict = {(0, 0): 0, (0, 1): 1, (0, 2): 2,
                (1, 0): 4, (1, 1): 5, (1, 2): 6,
                (2, 0): 8, (2, 1): 9, (2, 2): 10}
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'X'
                if check(board):
                    return idx_dict[(i, j)]
                board[i][j] = 'O'
                if check(board):
                    return idx_dict[(i, j)]
                board[i][j] = '-'

            # keep this function call here


print(GameChallenge(input()))