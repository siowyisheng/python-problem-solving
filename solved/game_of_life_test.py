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

import pytest
from game_of_life import *


@pytest.mark.parametrize(
    'board,steps,expected',
    [([(0, 0)], 0, '*\n\n'),
     ([(0, 0), (1, 0)], 0, '**\n\n'),
     ([(0, 0), (0, 1)], 0, '*\n*\n\n'),
     ([(0, 0), (0, 1), (1, 0), (1, 1)], 0, '**\n**\n\n'),
     ([(1, 0), (0, 1)], 0, '*.\n.*\n\n'),
     ([(0, 0)], 1, '\n\n'),
     ([(0, 0), (1, 0), (0, 1)], 1, '**\n**\n\n'),
     ([(0, 0), (1, 0), (0, 1)], 3, '**\n**\n\n**\n**\n\n**\n**\n\n'),
     ([(5, 5), (6, 5), (5, 6)], 3, '**\n**\n\n**\n**\n\n**\n**\n\n')])  # yapf: disable
def test_run_steps(board, steps, expected, capsys):
    run_steps(board, steps)
    captured = capsys.readouterr()
    assert captured.out == expected
