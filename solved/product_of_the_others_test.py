# Task: Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

import pytest
from product_of_the_others import *


@pytest.mark.parametrize("ls,expected",
                         [([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
                          ([0, 2, 3, 4, 5], [120, 0, 0, 0, 0]),
                          ([-1, 2, 3, 4, 5], [120, -60, -40, -30, -24]),
                          ([2 for i in range(50)], [2**49 for i in range(50)])]) # yapf: disable
def test_product_of_others(ls, expected):
    assert product_of_others(ls) == expected
