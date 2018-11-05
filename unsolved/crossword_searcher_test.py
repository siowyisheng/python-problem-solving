# Given a 2D matrix of characters and a target word, write a function that
# returns whether the word can be found in the matrix by going left-to-right, or up-to-down.
#
# For example, given the following matrix:
#
# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
# and the target word 'FOAM', you should return true, since it's the leftmost
# column. Similarly, given the target word 'MASS', you should return true,
# since it's the last row.

import pytest
from crossword_searcher import *


@pytest.mark.parametrize(
    'matrix, target, expected',
    [([['F', 'A', 'C', 'I'], ['O', 'B', 'Q', 'P'], ['A', 'N', 'O', 'B'],
       ['M', 'A', 'S', 'S']], 'FOAM', True),
     ([['F', 'A', 'C', 'I'], ['O', 'B', 'Q', 'P'], ['A', 'N', 'O', 'B'],
       ['M', 'A', 'S', 'S']], 'MASS', True),
     ([['F', 'A', 'C', 'I'], ['O', 'B', 'Q', 'P'], ['A', 'N', 'O', 'B'],
       ['M', 'A', 'S', 'S']], 'BOAT', False)])
def test_check_for_word(matrix, target, expected):
    assert check_for_word(matrix, target) == expected
