# Implement an autocomplete system. That is, given a query string s and a set of
# all possible query strings, return all strings in the set that have s as a prefix.

# Hint: Try preprocessing the dictionary into a more efficient data structure to
# speed up queries.

import pytest
from autocomplete import *


@pytest.mark.parametrize("q,set,expected",
                         [('de', ('dog', 'deer', 'deal'), ['deer', 'deal'])])
def test_autocomplete(q, set, expected):
    assert autocomplete(q, set) == expected
