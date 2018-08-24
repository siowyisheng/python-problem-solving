# Implement an autocomplete system. That is, given a query string s and a set of
# all possible query strings, return all strings in the set that have s as a prefix.

# Hint: Try preprocessing the dictionary into a more efficient data structure to
# speed up queries.


def autocomplete(q, set):
    letters = len(q)
    matches = [s for s in set if s[:letters] == q]
    return matches
