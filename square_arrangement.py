from cell_arrangement import CellArrangement
from line_arrangement import LineArrangement

class SquareArrangement(CellArrangement):

    def __init__(self, size):
        super().__init__(size)


    def arrange_relative(self, size, offset=0):
        offset = int(size / 2)
        return LineArrangement(size, offset=offset, vertical=True)\
            .add_to(LineArrangement(size, offset=-offset, vertical=True))\
            .add_to(LineArrangement(size, offset=offset, vertical=False))\
            .add_to(LineArrangement(size, offset=-offset, vertical=False)).cells