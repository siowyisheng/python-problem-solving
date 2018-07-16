# Task: Separate a list of elements, returning a 2d list with the inner lists having a specified length.

import pytest
from separate_into_batches import *


@pytest.mark.parametrize("ls,batch_size,expected", [
    ([i for i in range(100)], 128, [[i for i in range(100)]]),
    ([i for i in range(500)], 128,
     [[i for i in range(500)][:128], [i for i in range(500)][128:256],
      [i for i in range(500)][256:384], [i for i in range(500)][384:]]),
])
def test_separate_into_batches(ls, batch_size, expected):
    assert separate_into_batches(ls, batch_size) == expected
