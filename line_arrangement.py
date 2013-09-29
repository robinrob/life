from cell_arrangement import CellArrangement

class LineArrangement(CellArrangement):

    def __init__(self, size):
        super().__init__()


    def __init__(self, size, vertical=False):
        self.cells = self.arrange_relative(size, vertical)


    def arrange_relative(self, size, vertical=False):
        cells = []

        for i in range(size + 1):
            pos = int(i/2)
            if (i % 2):
                pos *= -1

            x = 0 if vertical else pos
            y = pos if vertical else 0

            cells.append((x, y))

        return cells