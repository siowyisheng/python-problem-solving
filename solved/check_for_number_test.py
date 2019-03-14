# Given a string, return whether it represents a number. Here are the different
# kinds of numbers:

#     "10", a positive integer
#     "-10", a negative integer
#     "10.1", a positive real number
#     "-10.1", a negative real number
#     "1e5", a number in scientific notation
#     And here are examples of non-numbers:

#         "a"
#         "x 1"
#         "a -2"
#         "-"

import pytest
from check_for_number import *


@pytest.mark.parametrize(
    's,expected',
    [
        ('10', True),
        ('-10', True),
        ('10.1', True),
        ('-10.1', True),
        ('1e5', True),
        ('a', False),
        ('x 1', False),
        ('a -2', False),
        ('-', False),
    ]
) #yapf:disable
def test_is_number(s, expected):
    assert is_number(s) == expected