from cell_arrangement import CellArrangement

class LineArrangement(CellArrangement):

    def __init__(self, size, offset=0):
        super().__init__(size, offset)


    def __init__(self, size, offset=0, vertical=False):
        self.cells = self.arrange_relative(size, offset, vertical)


    def arrange_relative(self, size, offset=0, vertical=False):
        cells = []

        for i in range(size + 1):
            pos = int(i/2)
            if (i % 2):
                pos *= -1

            x = offset if vertical else pos
            y = pos if vertical else offset

            cells.append((x, y))

        return cells