from cell_arrangement import CellArrangement
from grid_arrangement import GridArrangement
from line_arrangement import LineArrangement
from diagonal_arrangement import DiagonalArrangement
from cross_arrangement import CrossArrangement


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

#STARTING_ARRANGEMENT = CrossArrangement(10)

#STARTING_ARRANGEMENT = GridArrangement(10)

#STARTING_ARRANGEMENT = LineArrangement(5)

arr1 = DiagonalArrangement(10, flip=False)
arr2 = DiagonalArrangement(10, flip=True)
arr3 = LineArrangement(10, vertical=False)
arr4 = LineArrangement(10, vertical=True)

arr1.add_to(arr2).add_to(arr3).add_to(arr4)

STARTING_ARRANGEMENT = arr1

