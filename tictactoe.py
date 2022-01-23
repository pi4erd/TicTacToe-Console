from math import inf as infinity
from random import choice, randint

AI = 2
HUMAN = 1

EASY, MEDIUM, HARD, IMPOSSIBLE = 0, 1, 2, 3
DIFFICULTIES = [EASY, MEDIUM, HARD, IMPOSSIBLE]

def valid_move(board, x, y):
    return [x, y] in empty_cells(board)

def set_move(board, player, x, y):
    if valid_move(board, x, y):
        board[x][y] = player
        return True
    else:
        return False

def check_win_o(board):
    cols = board[0][0] == board[0][1] == board[0][2] == AI or \
        board[1][0] == board[1][1] == board[1][2] == AI or \
        board[2][0] == board[2][1] == board[2][2] == AI
    rows = board[0][0] == board[1][0] == board[2][0] == AI or \
        board[0][1] == board[1][1] == board[2][1] == AI or \
        board[0][2] == board[1][2] == board[2][2] == AI
    diags = board[0][0] == board[1][1] == board[2][2] == AI or \
        board[0][2] == board[1][1] == board[2][0] == AI
    return cols or rows or diags

def check_win_x(board):
    cols = board[0][0] == board[0][1] == board[0][2] == HUMAN or \
        board[1][0] == board[1][1] == board[1][2] == HUMAN or \
        board[2][0] == board[2][1] == board[2][2] == HUMAN
    rows = board[0][0] == board[1][0] == board[2][0] == HUMAN or \
        board[0][1] == board[1][1] == board[2][1] == HUMAN or \
        board[0][2] == board[1][2] == board[2][2] == HUMAN
    diags = board[0][0] == board[1][1] == board[2][2] == HUMAN or \
        board[0][2] == board[1][1] == board[2][0] == HUMAN
    return cols or rows or diags

def game_over(board):
    return check_win_x(board) or check_win_o(board)

def evaluate(board):
    if check_win_o(board):
        score = +1
    elif check_win_x(board):
        score = -1
    else:
        score = 0
    return score

def empty_cells(board):
    cells = []

    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells

def minimax(board, player, depth):
    if player == AI:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]
    
    if depth == 0 or game_over(board):
        score = evaluate(board)
        return [-1, -1, score]
    
    for cell in empty_cells(board):
        x, y = cell[0], cell[1]
        board[x][y] = player
        score = minimax(board, HUMAN if player == AI else AI, depth-1)
        board[x][y] = 0
        score[0], score[1] = x, y

        if player == AI:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score
        
    return best

def make_move(board, player, depth, difficulty):
    if difficulty == 3:
        return minimax(board, player, depth)
    elif difficulty == 2:
        mv = choice(empty_cells(board))
        mx, my = mv[0], mv[1]
        return [mx, my, 0] if 0 <= randint(0, 99) < 10 else minimax(board, player, depth)
    elif difficulty == 1:
        mv = choice(empty_cells(board))
        mx, my = mv[0], mv[1]
        return [mx, my, 0] if 0 <= randint(0, 99) < 40 else minimax(board, player, depth)
    else:
        mv = choice(empty_cells(board))
        mx, my = mv[0], mv[1]
        return [mx, my, 0]
