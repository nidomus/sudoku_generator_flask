from flask import Flask, jsonify
from datetime import datetime
from sudoku import Sudoku

app = Flask(__name__)


@app.route('/api/v1/generate/', methods=['GET'])
def generate_sudoku():

    sudoku = Sudoku()
    data = sudoku.get_json()
    response = jsonify(data)

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/api/v1/generate-easy/')
def generate_easy_game():

    sudoku = Sudoku()
    sudoku.generate_playable_board(max_empty_spaces=43)
    data = sudoku.get_json()

    response = jsonify(data)

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/api/v1/generate-medium/')
def generate_medium_game():

    sudoku = Sudoku()
    sudoku.generate_playable_board(max_empty_spaces=51)
    data = sudoku.get_json()

    return jsonify(data)


@app.route('/api/v1/generate-hard/')
def generate_hard_game():

    sudoku = Sudoku()
    sudoku.generate_playable_board(max_empty_spaces=58)
    data = sudoku.get_json()

    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
