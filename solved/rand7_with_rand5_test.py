# Using a function rand5() that returns an integer from 1 to 5 (inclusive) with
# uniform probability, implement a function rand7() that returns an integer from
# 1 to 7 (inclusive).
# ---------------------------------------------------------------------------------

from collections import Counter
import pytest

from rand7_with_rand5 import *


# bad way to test, but bad way is better than no way. can do mocking instead for better testing
def test_rand7():
    ls = [rand7() for i in range(700)]
    is_reasonably_random = True
    for i, x in Counter(ls).items():
        if x < 85:
            is_reasonably_random = False
    assert is_reasonably_random == True
