# Determine whether there exists a one-to-one character mapping from one string
# s1 to another s2.

# For example, given s1 = abc and s2 = bcd, return true since we can map a to b,
# b to c, and c to d.

# Given s1 = foo and s2 = bar, return false since the o cannot map to two
# characters.


def has_mapping(s1, s2):
    # for each letter, there should be one mapping
    if len(s1) != len(s2):
        return False
    mapping = {}
    for c1, c2 in zip(s1, s2):
        # need both to check for one-to-one mapping
        if c1 in mapping or c2 in mapping.values():
            try:
                if mapping[c1] != c2:
                    return False
            except KeyError:
                return False
        else:
            mapping[c1] = c2
    return True