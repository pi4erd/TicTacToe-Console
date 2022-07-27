#!/usr/bin/env python3

"""
TicTacToe game in console in python

Made by Devi
"""

from tictactoe import *
from client import *
from game import Game, State

def ask_exit_eng(code: int=0):
    input("Press Enter to exit...")
    exit(code)

def single_player_input(difficulty):
    board = [[0]*3 for _ in range(3)]
    while True:
        try:
            xw = check_win_x(board)
            ow = check_win_o(board)

            if xw or ow:
                clr_scr()
                txt = "x Won!" if xw else "o Won!"
                frq = 700 if xw else 400
                render_mtx(board)
                print(txt)
                print('\a')
                break

            if len(empty_cells(board)) == 0 and not game_over(board):
                clr_scr()
                render_mtx(board)
                print("Tie!")
                print('\a')
                break
            
            print('\a')

            clr_scr()
            render_mtx(board)
            print("You are 'x'\n")
            x = int(input("Choose column (1-3): ")) - 1
            y = int(input("Choose row (1-3): ")) - 1
            
            if not set_move(board, HUMAN, x, y):
                raise ValueError
            
            ai_output(board, difficulty)
        except ValueError or IndexError:
            clr_scr()
            print("Incorrect move! Try again...")
            input()

clientNumber = 0

def get_input(player: int, game: Game):
    done = False
    while not done:
        try:
            clr_scr()
            render_mtx_multiplayer(game.board)
            print("You are '{}'\n".format(sf_multi(player)))
            x = int(input("Choose column (1-3): ")) - 1
            y = int(input("Choose row (1-3): ")) - 1

            game.play(player, f"{x}{y}")
            
            done = True
            return f"{x}{y}"
        except ValueError or IndexError:
            clr_scr()
            print("Incorrect move! Try again...")
            input()

if __name__ == "__main__":
    while True:
        clr_scr()
        mode = input("Choose mode to play (multi/single): ")
        if mode == "multi":
            n = Network("localhost", 8080)
            player = int(n.get_player())
            clr_scr()
            print("You are", sf_multi(player))
            print("Wait for your turn...")
            ended = False   
            while not ended:
                try:
                    game: Game = n.send("get")
                except:
                    print("Couldn't get game")
                    ask_exit_eng(-1)
                
                if game.turn == player:
                    state = game.getstate()
                    if state == State.get_state_from_player(player):
                        print("You won!")
                        ended = True
                        continue
                    elif state == State.get_state_from_player(player ^ 1):
                        print("You lost!")
                        ended = True
                        continue
                    elif state == State.TIE:
                        print("Tie!")
                        ended = True
                        continue
                    
                    n.send(get_input(player, game))
                    
                    clr_scr()
                    render_mtx_multiplayer(game.board)
                    print(f"'{sf_multi(player ^ 1)}' turn")
                    state = game.getstate()
                    if state == State.get_state_from_player(player):
                        print("You won!")
                        ended = True
                        continue
                    elif state == State.get_state_from_player(player ^ 1):
                        print("You lost!")
                        ended = True
                        continue
                    elif state == State.TIE:
                        print("Tie!")
                        ended = True
                        continue
                    print("Waiting for other player...")
            ask_exit_eng()
        elif mode == "single":
            clr_scr()
            diff = int(input("Please, write difficulty (0-3): "))
            if not diff in DIFFICULTIES and diff != -1:
                clr_scr()
                input("Incorrect difficulty! Try again...")
                continue
            elif diff == -1:
                ask_exit_eng()
            single_player_input(diff)
            ask_exit_eng()
        else:
            input("Incorrect mode! Try again...")
    