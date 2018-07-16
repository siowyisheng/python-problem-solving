# Task: Determine if any two numbers from a list of numbers add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


def any_two_add_up(ls, k):
    if len(ls) < 2:
        print('The list must have at least two numbers.')
    targets = []
    for i in ls:
        if i in targets:
            return True
        else:
            targets.append(k - i)
    return False
