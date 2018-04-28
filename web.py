from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import game

app = Flask(__name__)

current_game = game.GameBoard()
current_game.build_play_board(6)
current_game.set_ship(3)

@app.route('/')
def index():
    return render_template('index.html', my_board=current_game.get_play_board())

@app.route('/', methods=['POST'])
def make_guess():
    try:
        x = int(request.form['x'])
        y = int(request.form['y'])
    except ValueError:
        return render_template('index.html', my_board=current_game.get_play_board(), input_error='*form only accepts numbers*')

    current_ship_board = current_game.get_ship_board()


    if current_game.check_for_hit(x, y):
        return render_template('index.html', my_board=current_ship_board)
    else:
        current_game.update_play_board(x, y)
        return render_template('index.html', my_board=current_game.get_play_board())


if __name__ == '__main__':
    app.debug = True
    app.config['SECRET_KEY'] = 'YWJjZGVmZw=='
    toolbar = DebugToolbarExtension(app)

    app.run(host='0.0.0.0', port=8080)