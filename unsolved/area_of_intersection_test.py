# Given two rectangles on a 2D graph, return the area of their intersection. If the
# rectangles don't intersect, return 0.

# For example, given the following rectangles:

#     {
#         "top_left": (1, 4),
#             "dimensions": (3, 3) # width, height
#             }
#             and

#             {
#                 "top_left": (0, 5),
#                     "dimensions" (4, 3) # width, height
#                     }
#                     return 6.

import pytest
from area_of_intersection import *


@pytest.mark.parametrize(
    'r1,r2,expected', [
    ([(1,4),(3,3)],[(0,5),(4,3)], 6),
]) # yapf: disable
def test_intersection_area(r1, r2, expected):
    assert intersection_are(r1, r2) == expected