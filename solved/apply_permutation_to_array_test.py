# A permutation can be specified by an array P, where P[i] represents the
# location of the element at i in the permutation. For example, [2, 1, 0]
# represents the permutation where elements at the index 0 and 2 are swapped.

# Given an array and a permutation, apply the permutation to the array. For
# example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return
# ["c", "b", "a"].

import pytest
from apply_permutation_to_array import *


@pytest.mark.parametrize(
    'array,permutation,expected', [
    (['a','b','c'], [2,1,0], ['c','b','a']),
    (['a','b','c'], [0,1,2], ['a','b','c'])
]) # yapf: disable
def test_permutate_array(array, permutation, expected):
    assert permutate_array(array, permutation) == expected