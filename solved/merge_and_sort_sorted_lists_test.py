# Task : Return a new sorted merged list from K sorted lists, each with size N.
# For example, if we had [[10, 15, 30], [12, 15, 20], [17, 20, 32]], the result should be [10, 12, 15, 15, 17, 20, 20, 30, 32].

import pytest
from merge_and_sort_sorted_lists import *


@pytest.mark.parametrize("lists,expected", [
    ([[10, 15, 30], [12, 15, 20], [17, 20, 32]], [10, 12, 15, 15, 17, 20, 20, 30, 32]),
    ([[1, 50, 51], [2, 42, 43], [3, 99, 200]], [1, 2, 3, 42, 43, 50, 51, 99, 200]),
]) # yapf: disable
def test_merge_and_sort_sorted_lists(lists, expected):
    assert merge_and_sort_sorted_lists(lists) == expected
