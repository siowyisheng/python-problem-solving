# Task: Determine if any two numbers from a list of numbers add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

import pytest
from any_two_add_up_to_k import *


@pytest.mark.parametrize(
    "ls,k,expected", [([10, 15, 3, 7], 17, True),
                      ([10, 15, 3, 7], 18, True),
                      ([10, 15, 3, 7], 50, False),
                      ([-1, 3, 5, 7], 4, True),
                      ([i for i in range(100)], 107, True),
                      ([i for i in range(1000)], 1997, True)]) # yapf: disable
def test_any_two_add_up(ls, k, expected):
    assert any_two_add_up(ls, k) == expected
