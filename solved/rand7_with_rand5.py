# Using a function rand5() that returns an integer from 1 to 5 (inclusive) with
# uniform probability, implement a function rand7() that returns an integer from
# 1 to 7 (inclusive).
# ---------------------------------------------------------------------------------

# we just treat each number from 1 to 7 as a player rolling off with a 5 sided die!

import random


def rand7():
    return roll_off(range(1, 8))


def roll_off(contenders):
    scores = [rand5() for i in contenders]
    tied_contenders = [
        contenders[i] for i, x in enumerate(scores) if x == max(scores)
    ]
    if len(tied_contenders) == 1:
        return tied_contenders[0]
    else:
        return roll_off(tied_contenders)


def rand5():
    return random.randint(1, 5)
