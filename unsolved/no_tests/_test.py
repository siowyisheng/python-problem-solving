import pytest
from cheapest_paint_houses import *


@pytest.mark.parametrize('input,expected', [(1, 2), (3, 4)])
def test_funcname(input, expected):
    assert funcname(input) == expected
