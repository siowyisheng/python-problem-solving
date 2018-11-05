# On our special chessboard, two bishops attack each other if they share the same
# diagonal. This includes bishops that have another bishop located between them,
# i.e. bishops can attack through pieces.
#
# You are given N bishops, represented as (row, column) tuples on a M by
# M chessboard. Write a function to count the number of pairs of bishops that
# attack each other. The ordering of the pair doesn't matter: (1, 2) is
# considered the same as (2, 1).
#
# For example, given M = 5 and the list of bishops:
#
#     (0, 0)
#     (1, 2)
#     (2, 2)
#     (4, 0)
#     The board would look like this:
#
#     [b 0 0 0 0]
#     [0 0 b 0 0]
#     [0 0 b 0 0]
#     [0 0 0 0 0]
#     [b 0 0 0 0]

import pytest
from bishops_on_board import *


@pytest.mark.parametrize('M,bishop_coordinates,expected',
                         [(5, [(0, 0), (1, 2), (2, 2), (4, 0)], 2)])
def test_count_bishop_pairs_attacking_each_other(M, bishop_coordinates,
                                                 expected):
    assert count_bishop_pairs_attacking_each_other(
        M, bishop_coordinates) == expected
