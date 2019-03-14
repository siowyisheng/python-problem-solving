# Determine whether there exists a one-to-one character mapping from one string
# s1 to another s2.

# For example, given s1 = abc and s2 = bcd, return true since we can map a to b,
# b to c, and c to d.

# Given s1 = foo and s2 = bar, return false since the o cannot map to two
# characters.

import pytest
from character_mapping import *

@pytest.mark.parametrize(
    's1,s2,expected',
    [
        ('shiftedmessage', 'tijgsfenfttbhf', True),
        ('abc', 'bcd', True),
        ('aba', 'bcd', False),
        ('abc', 'ddd', False),
        ('abc', 'bcc', False),
        ('foo', 'bar', False),
    ]
) #yapf:disable
def test_has_mapping(s1, s2, expected):
    assert has_mapping(s1, s2) == expected
