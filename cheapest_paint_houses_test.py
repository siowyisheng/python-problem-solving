# A builder is looking to build a row of N houses that can be of K different
# colors. He has a goal of minimizing cost while ensuring that no two
# neighboring houses are of the same color.
#
# Given an N by K matrix where the nth row and kth column represents the cost
# to build the nth house with kth color, return the minimum cost which achieves
# this goal.

import pytest
from cheapest_paint_houses import *


@pytest.mark.parametrize('input,expected',
                         [([[1, 2], [2, 1]], 2),
                          ([[1, 5, 7], [1, 3, 2], [2, 2, 2], [1, 5, 6]], 6)])
def test_minimum_cost(input, expected):
    assert minimum_cost(input) == expected
