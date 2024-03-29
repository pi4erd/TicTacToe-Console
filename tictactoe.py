import os
from math import inf as infinity
from random import choice, randint
import platform

AI = 2
HUMAN = 1

EASY, MEDIUM, HARD, IMPOSSIBLE = 0, 1, 2, 3
DIFFICULTIES = [EASY, MEDIUM, HARD, IMPOSSIBLE]

def valid_move(board, x, y):
    return [x, y] in empty_cells(board)

def valid_move_multi(board, x, y):
    return [x, y] in empty_cells_multi(board)

def set_move(board, player, x, y):
    if valid_move(board, x, y):
        board[x][y] = player
        return True
    else:
        return False

def set_move_multi(board, player, x, y):
    if valid_move_multi(board, x, y):
        board[x][y] = player
        return True
    else:
        return False
def sf_multi(s: int):
    l = [' ', 'x', 'o'] # -1 0 1
    return l[s + 1]

def sf(s):
    l = [' ', 'x', 'o']
    return l[s]

def render_mtx(m):
    print(f"""{sf(m[0][0])}|{sf(m[1][0])}|{sf(m[2][0])}
{sf(m[0][1])}|{sf(m[1][1])}|{sf(m[2][1])}
{sf(m[0][2])}|{sf(m[1][2])}|{sf(m[2][2])}
""")
def render_mtx_multiplayer(m):
    print(f"""{sf_multi(m[0][0])}|{sf_multi(m[1][0])}|{sf_multi(m[2][0])}
{sf_multi(m[0][1])}|{sf_multi(m[1][1])}|{sf_multi(m[2][1])}
{sf_multi(m[0][2])}|{sf_multi(m[1][2])}|{sf_multi(m[2][2])}
""")
def clr_scr():
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Darwin":
        os.system("clear")
    else:
        raise NotImplementedError("Current platform '{}' is not supported yet".format(platform.system()))
def ai_output(board, difficulty):
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return
    
    clr_scr()
    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = make_move(board, AI, depth, difficulty)
        x, y = move[0], move[1]
    set_move(board, AI, x, y)

def check_win(board, p):
    cols = board[0][0] == board[0][1] == board[0][2] == p or \
        board[1][0] == board[1][1] == board[1][2] == p or \
        board[2][0] == board[2][1] == board[2][2] == p
    rows = board[0][0] == board[1][0] == board[2][0] == p or \
        board[0][1] == board[1][1] == board[2][1] == p or \
        board[0][2] == board[1][2] == board[2][2] == p
    diags = board[0][0] == board[1][1] == board[2][2] == p or \
        board[0][2] == board[1][1] == board[2][0] == p
    return cols or rows or diags

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
    return check_win_o(board) or check_win_x(board)

def game_over_multi(board, players):
    return check_win(board, players[0]) or check_win(board, players[1])

def evaluate(board):
    if check_win_o(board):
        score = +1
    elif check_win_x(board):
        score = -1
    else:
        score = 0
    return score

def empty_cells_multi(board):
    cells = []

    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell == -1:
                cells.append([x, y])

    return cells

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
