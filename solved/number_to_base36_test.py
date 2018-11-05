# Task: Take a one-indexed number and output a one-indexed base-36 string.

import pytest
from number_to_base36 import *


@pytest.mark.parametrize("num,expected",
                         [(1,'0'),
                         (10,'9'),
                         (11,'a'),
                         (1764102650123,'af350ehl')]) # yapf: disable
def test_to_b36(num, expected):
    assert to_b36(num) == expected
