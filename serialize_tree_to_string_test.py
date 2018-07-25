# Task: Given the root to a binary tree, implement serialize(root), which
# serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
#
# For example, given the following Node class
#
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

import pytest
from serialize_tree_to_string import *


# @pytest.mark.parametrize(
#     "ls,expected", [([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
#                     ([0, 2, 3, 4, 5], [120, 0, 0, 0, 0]),
#                     ([-1, 2, 3, 4, 5], [120, -60, -40, -30, -24]),
#                     ([2 for i in range(50)], [2**49 for i in range(50)])])
def test_serialize_tree_to_string(ls, expected):
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
