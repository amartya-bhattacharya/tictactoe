import numpy as np


def print_board(board):
    print("---------")
    print("|", board[0][0], board[0][1], board[0][2], "|")
    print("|", board[1][0], board[1][1], board[1][2], "|")
    print("|", board[2][0], board[2][1], board[2][2], "|")
    print("---------")


def check_rows(board, player):
    for row in board:
        if len(set(row)) == 1:
            if row[0] == player:
                return True
    return False


def check_diagonals(board, player):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        if board[0][0] == player:
            return True
    if len(set([board[i][len(board) - i - 1] for i in range(len(board))])) == 1:
        if board[0][len(board) - 1] == player:
            return True
    return False


def check_win(board):
    # transposition to check rows, then columns
    for new_board in [board, np.transpose(board)]:
        x_result = check_rows(new_board, 'X')
        o_result = check_rows(new_board, 'O')
        if x_result and o_result:
            return 'I'
        if x_result:
            return 'X'
        elif o_result:
            return 'O'
    if check_diagonals(board, 'X'):
        return 'X'
    elif check_diagonals(board, 'O'):
        return 'O'


def check_empty(board):
    for x in board:
        for y in x:
            if y == "_":
                return True
    return False


def check_diff(board):
    x_count = 0
    o_count = 0
    for x in board:
        for y in x:
            if y == 'X':
                x_count += 1
            if y == 'O':
                o_count += 1
    return abs(x_count - o_count)


def check_state(board):
    winner = check_win(board)
    if check_diff(board) >= 2 or winner == 'I':
        print("Impossible")
        return 1
    if not winner:
        if check_empty(board):
            return 0
        else:
            print("Draw")
            return 1
    else:
        print(winner, "wins")
        return 1


def input_board():
    board_input = input("Enter cells: ")

    in_grid = []
    for i in range(3):
        in_grid.append(list(board_input[i * 3:i * 3 + 3]))

    return in_grid


def make_move(board, player):
    try:
        x, y = [int(i) - 1 for i in input("Enter the coordinates: ").split()]
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Coordinates should be from 1 to 3!")
            return make_move(board, player)
        elif board[x][y] != '_':
            print("This cell is occupied! Choose another one!")
            return make_move(board, player)
        else:
            board[x][y] = player
            return board
    except ValueError:
        print("You should enter numbers!")
        return make_move(board, player)


grid = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
players = ['X', 'O']
print_board(grid)
i = 0
while not check_state(grid):
    player = players[i]
    i = (i + 1) % 2
    change_board = make_move(grid, player)
    print_board(change_board)
