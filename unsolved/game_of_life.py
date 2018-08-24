# Conway's Game of Life takes place on an infinite two-dimensional board of
# square cells. Each cell is either dead or alive, and at each tick, the
# following rules apply:
#
# Any live cell with less than two live neighbours dies.
# Any live cell with two or three live neighbours remains living.
# Any live cell with more than three live neighbours dies.
# Any dead cell with exactly three live neighbours becomes a live cell.
# A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.
#
# Implement Conway's Game of Life. It should be able to be initialized with a
# starting list of live cell coordinates and the number of steps it should run
# for. Once initialized, it should print out the board state at each step.
# Since it's an infinite board, print out only the relevant coordinates, i.e.
# from the top-leftmost live cell to bottom-rightmost live cell.
#
# You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
from __future__ import print_function


# simplify coordinates somewhere?
def run_steps(board, steps):
    str_board = stringify(board)
    for i in range(steps):
        board = generate_next_board(board)
        print(str_board)
    if not steps:
        print(str_board)


def get_width_height(board):
    x_coords = [cell[0] for cell in board]
    y_coords = [cell[1] for cell in board]
    width = max(x_coords) - min(x_coords) + 1
    height = max(y_coords) - min(y_coords) + 1
    return width, height


def stringify(board):
    width, height = get_width_height(board)
    s = ''
    for j in range(height):
        line = ''
        for i in range(width):
            if (i, j) in board:
                line += '*'
            else:
                line += '.'
        s = '\n' + line + s
    s = s[1:]
    return s


def generate_next_board(board):
    width, height = get_width_height(board)
    candidate_for_life = set()
    for live_cell in board:
        x, y = live_cell
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                candidate_for_life += (x + i, y + j)
    new_board = []
    for cell in candidate_for_life:
        n = count_live_neighbours(cell)
        if cell in board and n in (2, 3):
            new_board.append(cell)
        if cell not in board and n == 3:
            new_board.append(cell)


def count_live_neighbours(cell, board):
    pass


# Any live cell with less than two live neighbours dies.
# Any live cell with two or three live neighbours remains living.
# Any live cell with more than three live neighbours dies.
# Any dead cell with exactly three live neighbours becomes a live cell.
# A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.
