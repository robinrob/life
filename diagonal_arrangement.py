from cell_arrangement import CellArrangement

class DiagonalArrangement(CellArrangement):

    def __init__(self, size):
        super().__init__()


    def __init__(self, size, flip=False):
        self.cells = self.arrange_relative(size, flip)


    def arrange_relative(self, size, flip=False):
        cells = []

        for i in range(size):
            pos = int(i / 2)
            if (i % 2):
                pos *= -1

            x = pos
            y = pos if not flip else -1 * pos

            cells.append((x, y))

        return cells