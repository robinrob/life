from cell_arrangement import CellArrangement
from diagonal_arrangement import DiagonalArrangement

class CrossArrangement(CellArrangement):

    def __init__(self, size):
        super().__init__(size)


    def arrange_relative(self, size):
        cells = []
        for cell in DiagonalArrangement(size, False).cells:
            cells.append(cell)

        for cell in DiagonalArrangement(size, True).cells:
            cells.append(cell)

        return cells