# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
#
# For example, given the string "([])[]({})", you should return true.
#
# Given the string "([)]" or "((()", you should return false.

import pytest
from balanced_brackets import *


@pytest.mark.parametrize("s,expected", [("([])[]({})", True), ("([)]", False),
                                        ("((()", False)])
def test_balanced_brackets(s, expected):
    assert balanced_brackets(s) == expected
