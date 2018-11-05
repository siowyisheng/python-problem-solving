# Suppose you are given a table of currency exchange rates, represented as a
# 2D array. Determine whether there is a possible arbitrage: that is, whether
# there is some sequence of trades you can make, starting with some amount A
# of any currency, so that you can end up with some amount greater than A of
# that currency.
#
# There are no transaction costs and you can trade fractional quantities.

import pytest
from detect_arbitrage import *


@pytest.mark.parametrize('input,expected', [(1, 2), (3, 4)])
def test_determine_arbitrage_possibility(input, expected):
    assert determine_arbitrage_possibility(input) == expected
