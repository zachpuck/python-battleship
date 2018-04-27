import random


g = 3 # grid size
s = 1 # ship size (currently only 1 space)

class GameBoard(object):
    """
    setup and interact with game grid
    """
    def __init__(self):
        self.size = None
        self.board = []

    def get_board(self):
        return self.board

    def build_board(self, g):
        for i in range( 0, g):
            self.board.append([])
        
        for i in range(g):
            self.board[i].extend('O' for i in range(g))

    def set_ship(self, s):
        x = random.randint(0, g)
        y = random.randint(0, g)
        self.board[x][y] = 's'

    def check_for_hit(self, x, y):
        if self.board[x][y] == 's':
            return True
        else:
            return False

play = GameBoard()
play.build_board(g)
play.set_ship(s)