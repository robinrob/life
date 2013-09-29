from cell_arrangement import CellArrangement
from grid_arrangement import GridArrangement
from line_arrangement import LineArrangement
from diagonal_arrangement import DiagonalArrangement
from diagonal_cross_arrangement import DiagonalCrossArrangement
from square_cross_arrangement import SquareCrossArrangement
from square_arrangement import SquareArrangement


#LIVE = chr(169)
LIVE = "x"
DEAD = " "


#CELLS = [(-1, 1), (0, 1), (1, 1)]

# Qaudruple dual-oscillator
#CELLS = [(-1, 1), (0, 1), (1, 1),
#         (-1, 0), (0, 0), (1, 0),
#         (-1, -1), (0, -1), (1, -1)]


# This one reaches a stable structure after 3 turns!
#CELLS = [(0, 1), (1, 1),
#         (1, 0), (2, 0)]


# Wow, four stable structures
#CELLS = [(-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1),
#         (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0),
#         -2, -1), (-1, -1), (0, -1), (1, -1), (2, -1)]

STARTING_ARRANGEMENT = DiagonalCrossArrangement(10)

#STARTING_ARRANGEMENT = SquareCrossArrangement(10)

#STARTING_ARRANGEMENT = GridArrangement(10)

#STARTING_ARRANGEMENT = LineArrangement(5, offset=5)

#STARTING_ARRANGEMENT = SquareArrangement(10)

# Configurations can be added together like this:
#arr1 = DiagonalArrangement(10, flip=False)
#arr2 = DiagonalArrangement(10, flip=True)
#arr3 = LineArrangement(10, vertical=False)
#arr4 = LineArrangement(10, vertical=True)

#arr1.add_to(arr2).add_to(arr3).add_to(arr4)

#arr = []
#arr.append(LineArrangement(10, offset=5, vertical=True))
#arr.append(LineArrangement(10, offset=-5, vertical=True))
#arr.append(LineArrangement(10, offset=5, vertical=False))
#arr.append(LineArrangement(10, offset=-5, vertical=False))
#arr.append(DiagonalArrangement(10, flip=False))
#arr.append(DiagonalArrangement(10, flip=True))
#
#for i in range(0, len(arr) - 1):
#    arr[0].add_to(arr[i + 1])

#STARTING_ARRANGEMENT = arr

