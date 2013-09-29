from cell_arrangement import CellArrangement

class GridArrangement(CellArrangement):

    def __init__(self, size):
        super().__init__(size)


    def arrange_relative(self, size):
        cells = []
        for i in range(size):
            for j in range(size):
                cells.append((i, j))

        return cells