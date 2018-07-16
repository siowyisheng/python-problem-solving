# Task: Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

import numpy as np


def product_of_others(ls):
    new_ls = []
    for i in ls:
        ls2 = ls.copy()
        ls2.remove(i)
        ls_without_i_element = ls2
        new_ls.append(np.prod(ls_without_i_element))
    return new_ls
