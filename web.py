from flask import Flask
import game

app = Flask(__name__)

@app.route('/')
def index():
    load_game = game.GameBoard()
    load_game.build_board(6)
    load_game.set_ship(3)

    current_board = load_game.get_board()
    print_grid = ''
    for i in range(len(current_board)):
        for space in current_board[i]:
            print_grid += space + '\n'

    print(print_grid)
    return print_grid

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)