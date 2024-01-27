from flask import Flask, jsonify
from datetime import datetime
from sudoku import Sudoku

app = Flask(__name__)


@app.route('/generateSudoku/')
def generateSudoku():

    sudoku = Sudoku()
    sudoku.preencher_tabuleiro()
    data = sudoku.get_json_tabuleiro()

    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
