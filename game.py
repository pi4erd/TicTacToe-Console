from enum import Enum
from tictactoe import *

class State(Enum):
    ACTIVE = 0
    XWON = 1
    OWON = 2
    TIE = 3

    @staticmethod
    def get_state_from_player(p: int):
        return State.XWON if p == 0 else State.OWON

class Game:
    def __init__(self, id):
        self.id = id
        self.board = [[-1]*3 for _ in range(3)]
        self.ready = False
        self.state = State.ACTIVE
        self.turn = 0

    def get_board(self):
        return self.board
    
    def play(self, player, move: str):
        if player != self.turn:
            return False
        if not set_move_multi(self.board, player, int(move[0]), int(move[1])):
            return False
        self.turn = self.turn ^ 1
        return True

    def winner(self):
        p1 = check_win(self.board, 0)
        p2 = check_win(self.board, 1)

        if p1 or p2:
            self.state = State.XWON if p1 else State.OWON
            return 0 if p1 else 1

        return -1

    def getstate(self):
        self.winner()
        return self.state

    def connected(self):
        return self.ready
    
    def your_turn(self, p):
        return self.turn == p

    def reset(self):
        self.board = [[0]*3 for _ in range(3)]
        self.ready = False
        self.state = State.NOTREADY
        self.turn = 0