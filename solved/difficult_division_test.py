# Implement division of two positive integers without using the division,
# multiplication, or modulus operators. Return the quotient as an integer,
# ignoring the remainder.

import pytest
from difficult_division import *


@pytest.mark.parametrize(
    'number,divisor,expected', [
    (10, 2, 5),
    (21, 3, 7),
    (8, 3, 2),
]) # yapf: disable
def test_difficult_division(number, divisor, expected):
    assert difficult_division(number, divisor) == expected