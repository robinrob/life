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

#STARTING_ARRANGEMENT = DiagonalCrossArrangement(10)

#STARTING_ARRANGEMENT = SquareCrossArrangement(10)

#STARTING_ARRANGEMENT = GridArrangement(10)

#STARTING_ARRANGEMENT = LineArrangement(5, offset=5)

#STARTING_ARRANGEMENT = SquareArrangement(10)

# Configurations can be added together like this:
#STARTING_ARRANGEMENT = SquareArrangement(10)\
#    .add_to(SquareCrossArrangement(10))

STARTING_ARRANGEMENT = SquareArrangement(10)\
    .add_to(DiagonalCrossArrangement(10))

#STARTING_ARRANGEMENT = SquareCrossArrangement(10)\
#    .add_to(DiagonalCrossArrangement(10))