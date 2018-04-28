import random


g = 6 # grid size
s = 3 # ship size

class GameBoard(object):
    """
    setup and interact with game grid
    """
    def __init__(self):
        self.size = None
        self.play_board = []
        self.ship_board = None

    def get_play_board(self):
        return self.play_board
    def update_play_board(self, x, y):
        self.play_board[x][y] = 'm'

    def get_ship_board(self):
        return self.ship_board

    def build_play_board(self, g):
        for i in range( 0, g):
            self.play_board.append([])
        
        for i in range(g):
            self.play_board[i].extend('O' for i in range(g))

    def set_ship(self, s):
        x = random.randint(0, g-1)
        y = random.randint(0, g-1)

        self.ship_board = [spaces[:] for spaces in self.play_board] # self.ship_board = copy.deepcopy(play_board)

        try:
            for i in range(s):
                self.ship_board[x+i][y] = 'S'
        except IndexError:
            pass

    def check_for_hit(self, x, y):
        if self.ship_board[x][y] == 'S':
            return True
        else:
            return False

    def find_ship(self):
        for i in range(g):
            for j in range(0, g, s):
                if self.check_for_hit(i,j):
                    print('You sunk my battleship!', i, j)
