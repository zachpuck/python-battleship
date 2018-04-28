import sys
import logging
import datetime
from flask import Flask, render_template, request
import game

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

current_game = game.GameBoard()
current_game.build_play_board(6)
current_game.set_ship(3)

@app.route('/')
def index():
    app.logger.info('Information: Game started at %s', datetime.datetime.now())
    return render_template('index.html', my_board=current_game.get_play_board())

@app.route('/', methods=['POST'])
def make_guess():
    current_ship_board = current_game.get_ship_board()

    try:
        x = int(request.form['x'])
        y = int(request.form['y'])
    except ValueError:
        return render_template('index.html', my_board=current_game.get_play_board(), input_error='*form only accepts numbers*')

    try:
        if current_game.check_for_hit(x, y):
            return render_template('index.html', my_board=current_ship_board)
        else:
            current_game.update_play_board(x, y)
            return render_template('index.html', my_board=current_game.get_play_board())
    except IndexError as e:
        app.logger.warning('guess outside of grid %s', e)
        return render_template('index.html', my_board=current_game.get_play_board(), input_error='*coordinates off map, guess again.*')

####################
## Error Handling ##
####################
@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('Page not found: %s', (request.path))
    return render_template('404.html'), 404

@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception: %s', (e))
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.debug = True
    app.config['SECRET_KEY'] = 'YWJjZGVmZw=='
    toolbar = DebugToolbarExtension(app)

    app.run(host='0.0.0.0', port=8080)
