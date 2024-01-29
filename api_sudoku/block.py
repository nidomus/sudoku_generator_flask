from random import shuffle
import copy


class BlockedException(Exception):
    pass


class Block():

    def __init__(self, id) -> None:

        self.id = id
        self.matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.vertical_neighbors: list[Block] = []
        self.horizontal_neighbors: list[Block] = []

    # Fill the block following the rules of Sudoku
    def fill_block(self):

        while self.verify_block(0):

            self.matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            shuffle(numbers)

            for row in range(3):

                for column in range(3):
                    for num in numbers:
                        if not self.verify_neighbors(num, row, column):
                            self.matrix[row][column] = num
                            numbers.remove(num)
                            break

            if len(numbers) > 0:
                raise BlockedException

    def get_remaining_numbers(self,):

        numbers = []
        for i in self.matrix:
            for j in i:
                numbers.append(j)

        full_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        remaing_list = []

        for x in full_list:
            if x not in numbers:
                remaing_list.append(x)

        return remaing_list

    # Verify if the drawn number is already in this block
    def verify_block(self, value):

        for row in self.matrix:
            if value in row:
                return True

        return False

    def find_invalid_numbers(self, value, row, column):
        coordinates = []

        for neighbor in self.horizontal_neighbors:
            aux = neighbor.verify_row(value, row)
            if aux is not None:
                coordinates.append(aux)

        for neighbor in self.vertical_neighbors:
            aux = neighbor.verify_column(value, column)
            if aux is not None:
                coordinates.append(aux)
        return coordinates

    # Verify if the drawn number obey the neighbors rule of Sudoku

    def verify_neighbors(self, value, row, column):

        for neighbor in self.horizontal_neighbors:
            if neighbor.verify_row(value, row) is not None:
                return True

        for neighbor in self.vertical_neighbors:
            if neighbor.verify_column(value, column) is not None:
                return True

        return False

    def count_value(self, value):
        qtd = 0
        for row in range(3):
            for column in range(3):
                if self.matrix[row][column] == value:
                    qtd += 1
        return qtd

    def verify_row(self, value, row):
        if value in self.matrix[row]:
            i = row
            j = self.matrix[row].index(value)
            return (self.id, i, j)
        return None

    def verify_column(self, value, column):
        for row in self.matrix:
            if value == row[column]:
                i = self.matrix.index(row)
                j = column
                return (self.id, i, j)
        return None

    def get_number_coordinate(self, i, j):
        if self.id < 3:
            aux = 0
        elif self.id < 6:
            aux = 3
        else:
            aux = 6

        row = i + aux
        column = j + 3 * (self.id - aux)

        return (row, column)

    def set_horizontal_neighbors(self, neighbors):

        self.horizontal_neighbors = neighbors

    def set_vertical_neighbors(self, neighbors):

        self.vertical_neighbors = neighbors

    def __str__(self) -> str:

        string = ''

        for list in self.matrix:

            for number in list:

                string += str(number) + ' '
            string += '\n'

        return string
