from cell_arrangement import CellArrangement
from line_arrangement import LineArrangement

class SquareCrossArrangement(CellArrangement):

    def __init__(self, size):
        super().__init__(size)


    def arrange_relative(self, size, offset=0):
        return LineArrangement(size, vertical=False)\
            .add_to(LineArrangement(size, vertical=True)).cells