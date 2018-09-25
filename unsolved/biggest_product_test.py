# Given a list of integers, return the largest product that can be made by
# multiplying any three integers.
#
# For example, if the list is [-10, -10, 5, 2], we should return 500, since
# that's -10 * -10 * 5.
#
# You can assume the list has at least three integers.

import pytest
from biggest_product import *


@pytest.mark.parametrize('ls,expected',
                         [([-10, -10, 5, 2], 500),
                          ([10, -10, 5, 2], 100),
                          ([3, 4, 5], 60),
                          ([-10, -15, -20, 2, 10], 3000)]) # yapf: disable
def test_get_biggest_product(ls, expected):
    assert get_biggest_product(ls) == expected
