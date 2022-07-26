#!/usr/bin/env python3
from tictactoe import *

board = [[0]*3 for _ in range(3)]

def ask_exit(code: int=0):
    input("Нажмите Enter чтобы выйти...") # dull input to prevent from instant exit
    exit(code)

def player_input(difficulty):
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
                print('\a')
                break

            if len(empty_cells(board)) == 0 and not game_over(board):
                clr_scr()
                render_mtx(board)
                print("Ничья!")
                print('\a')
                break
            
            print('\a')

            clr_scr()
            render_mtx(board)
            print("Вы играете за 'x'\n")
            x = int(input("Выберите столбец (1-3): ")) - 1
            y = int(input("Выберите строку (1-3): ")) - 1
            
            if not set_move(board, HUMAN, x, y):
                raise ValueError
            
            ai_output(board, difficulty)
        except ValueError or IndexError:
            clr_scr()
            print("Это был неправильный ход. Попробуйте еще раз!")
            input()

while True:
    clr_scr()
    diff = int(input("Напишите сложность (0-3, 3 - самое сложное): "))
    if not diff in DIFFICULTIES and diff != -1:
        clr_scr()
        print("Неправильная сложность, попробуйте еще раз!")
        input()
        continue
    elif diff == -1:
        ask_exit()
    player_input(diff)
    ask_exit()
