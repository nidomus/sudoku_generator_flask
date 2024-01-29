from flask import Flask, jsonify
from datetime import datetime
from sudoku import Sudoku

app = Flask(__name__)


@app.route('/api/v1/generate-sudoku/')
def generate_sudoku():

    sudoku = Sudoku()
    sudoku.generate_sudoku()
    data = sudoku.get_json()

    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
