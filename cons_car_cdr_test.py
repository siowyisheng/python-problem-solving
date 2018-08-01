# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and
# last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#    return pair
# Implement car and cdr.

import pytest
from cons_car_cdr import *


@pytest.mark.parametrize("input,expected", [(cons(3, 4), 3)])
def test_car(input, expected):
    assert car(input) == expected


@pytest.mark.parametrize("input,expected", [(cons(3, 4), 4)])
def test_cdr(input, expected):
    assert cdr(input) == expected
