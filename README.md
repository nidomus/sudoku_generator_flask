# sudoku_generator_flask
 <h3>Flask API for generating sudokus games.</h3>


# Check out the endpoint in the link below

<a target='_blank'><h3>https://sudoku-generator.onrender.com/api/v1/generate/</h3></a>
<br>
<br>
# Structure of this API's JSON response

<h3>The base structure of the response JSON that represents a cell of the Sudoku board is:</h3>

```json
{ "data": [

 {
    "block": 4,
    "column": 4,
    "row": 4,
    "number": 5
},

]}
```

<br>

<h3>For a better comprehension, see the image bellow wich ilustrate all the JSON atributes on a sudoku board.</h3>
<br>
<br>
<div align="center"><img src="image.png" style=""></div>

<br>
<br>

<h3>I elaborated this structure for assist in validating user inputs in the development of the <a href='https://github.com/nidomus/YASG' target="_blank"><strong>YASG</strong></a> Project. With that information, I can easily validate whether the number inserted by the user in the position follows the rules of Sudoku by simply searching for duplicate numbers in the row, column, or block.</h3>
