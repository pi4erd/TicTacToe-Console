import os
from random import randint
from tictactoe import *
import winsound

board = [[0]*3 for _ in range(3)]
def sf(s):
    l = [' ', 'x', 'o']
    return l[s]
def render_mtx(m):
    print(f"""{sf(m[0][0])}|{sf(m[1][0])}|{sf(m[2][0])}
{sf(m[0][1])}|{sf(m[1][1])}|{sf(m[2][1])}
{sf(m[0][2])}|{sf(m[1][2])}|{sf(m[2][2])}
""")

# TODO: Create minimax based ai
def ai_output(): # lets fix AI
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return
    
    clr_scr()
    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, AI, depth)
        x, y = move[0], move[1]
    set_move(board, AI, x, y)

def clr_scr():
    os.system("cls")
def player_input():
    while True:
        try:

            xw = check_win_x(board)
            ow = check_win_o(board)

            if xw or ow:
                clr_scr()
                txt = "x Победил!" if xw else "o Победил!"
                frq = 700 if xw else 400
                render_mtx(board)
                print(txt)
                winsound.Beep(frq, 500)
                break

            if len(empty_cells(board)) == 0 and not game_over(board):
                clr_scr()
                render_mtx(board)
                print("Ничья!")
                winsound.Beep(500, 200)
                break
            
            winsound.Beep(600, 50)

            clr_scr()
            render_mtx(board)
            print("Вы играете за 'x'\n")
            x = int(input("Выберите столбец (1-3): ")) - 1
            y = int(input("Выберите строку (1-3): ")) - 1
            
            if not set_move(board, HUMAN, x, y):
                raise ValueError
            
            ai_output()
        except ValueError or IndexError:
            clr_scr()
            print("Это был неправильный ход. Попробуйте еще раз!")
            input()

player_input()
input("Нажмите Enter чтобы выйти...") # dull input to prevent from instant exit