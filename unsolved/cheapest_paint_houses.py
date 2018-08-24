# A builder is looking to build a row of N houses that can be of K different
# colors. He has a goal of minimizing cost while ensuring that no two
# neighboring houses are of the same color.
#
# Given an N by K matrix where the nth row and kth column represents the cost
# to build the nth house with kth color, return the minimum cost which achieves
# this goal.


def minimum_cost(matrix):
    min_cost = 0
    # houses = len(matrix)
    for house in matrix:
        min_cost += min(house)
    return min_cost
