import abc

class CellArrangement:

    def __init__(self, size):
        __metaclass__ = abc.ABCMeta
        self.cells = self.arrange_relative(size)


    @abc.abstractmethod
    def arrange_relative(self, size):
        return


    def arrange(self, width, height):
        new_cells = []
        for cell in self.cells:
            x = int(width / 2) + cell[0]
            y = -1 * (int(height / 2) + cell[1])
            new_cells.append((x, y))

        self.cells = new_cells
        return new_cells


    def add_to(self, arrangement):
        for cell in arrangement.cells:
            self.cells.append(cell)

        return self