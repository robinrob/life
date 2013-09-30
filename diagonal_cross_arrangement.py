from cell_arrangement import CellArrangement
from diagonal_arrangement import DiagonalArrangement

class DiagonalCrossArrangement(CellArrangement):

    def __init__(self, size):
        super().__init__(size)


    def arrange_relative(self, size, offset=0):
        return DiagonalArrangement(size, False)\
            .add_to(DiagonalArrangement(size, True)).cells