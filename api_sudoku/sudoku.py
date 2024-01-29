from block import Block, BlockedException
from random import randint


class Sudoku():
    def __init__(self) -> None:

        # Create the instance of the 9 blocks of sudoku board

        block_1 = Block(0)
        block_2 = Block(1)
        block_3 = Block(2)
        block_4 = Block(3)
        block_5 = Block(4)
        block_6 = Block(5)
        block_7 = Block(6)
        block_8 = Block(7)
        block_9 = Block(8)

        block_1.set_horizontal_neighbors([block_2, block_3])
        block_1.set_vertical_neighbors([block_4, block_7])

        block_2.set_horizontal_neighbors([block_1, block_3])
        block_2.set_vertical_neighbors([block_5, block_8])

        block_3.set_horizontal_neighbors([block_1, block_2])
        block_3.set_vertical_neighbors([block_6, block_9])

        block_4.set_horizontal_neighbors([block_5, block_6])
        block_4.set_vertical_neighbors([block_1, block_7])

        block_5.set_horizontal_neighbors([block_4, block_6])
        block_5.set_vertical_neighbors([block_2, block_8])

        block_6.set_horizontal_neighbors([block_4, block_5])
        block_6.set_vertical_neighbors([block_3, block_9])

        block_7.set_horizontal_neighbors([block_8, block_9])
        block_7.set_vertical_neighbors([block_1, block_4])

        block_8.set_horizontal_neighbors([block_7, block_9])
        block_8.set_vertical_neighbors([block_2, block_5])

        block_9.set_horizontal_neighbors([block_7, block_8])
        block_9.set_vertical_neighbors([block_3, block_6])

        self.blocks: list[Block] = [block_1, block_2, block_3,
                                    block_4, block_5, block_6, block_7, block_8, block_9]

        self.generate_board()

    def generate_board(self):

        flag = False
        while flag == False:
            flag = True
            for block in self.blocks:
                try:
                    block.fill_block()
                except BlockedException:
                    self.clear_blocks()
                    flag = False

    def generate_playable_board(self):

        empty_spaces = 0
        while empty_spaces <= 46:

            block_id = randint(0, 8)
            i = randint(0, 2)
            j = randint(0, 2)

            if self.blocks[block_id].matrix[i][j] != 0 and (self.blocks[block_id].count_value(0) < 8):
                self.blocks[block_id].matrix[i][j] = 0
                empty_spaces += 1

    def clear_blocks(self):
        for block in self.blocks:
            block.matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def get_json(self):

        json = {"data": []}

        blocks_range = 0
        while blocks_range < 9:

            blocks_range += 3

            for i in range(3):
                for j in range(blocks_range-3, blocks_range):
                    for k in range(0, 3):

                        row, column = self.blocks[j].get_number_coordinate(
                            i, k)

                        number = {
                            "number": self.blocks[j].matrix[i][k],
                            "row":  i,
                            "column": column,
                            "block": self.blocks[j].id
                        }

                        json['data'].append(number)

        return json
