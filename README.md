# sudoku_generator_flask
 Flask API for generating sudokus games.


# Check out the endpoint in the link below

<a>https://sudoku-generator.onrender.com/api/v1/generate/</a>


# Structure of this API's JSON response

The base structure of the response JSON that represents a cell of the Sudoku board is:

```
{ "data": [...

 {
    "block": 4,
    "column": 4,
    "row": 4,
    "number": 5
},

... ]}
```

For a better comprehension see the image bellow wich ilustrate all the atributes on a sudoku board.

!["Ilustration of this API JSON response structure in a sudoku board"]("./image.png")
