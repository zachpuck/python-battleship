import random


g = 6 # grid size
s = 3 # ship size

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
        x = random.randint(0, g-1)
        y = random.randint(0, g-1)

        try:
            for i in range(s):
                self.board[x+i][y] = 'S'
        except IndexError:
            pass

    def check_for_hit(self, x, y):
        if self.board[x][y] == 's':
            return True
        else:
            return False

    def find_ship(self):
        for i in range(g):
            for j in range(0, g, s):
                if self.check_for_hit(i,j):
                    print('You sunk my battleship!', i, j)

# play = GameBoard()
# play.build_board(g)
# play.set_ship(s)
# print(play.get_board())
# play.find_ship()