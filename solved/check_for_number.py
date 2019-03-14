# Given a string, return whether it represents a number. Here are the different
# kinds of numbers:

#     "10", a positive integer
#     "-10", a negative integer
#     "10.1", a positive real number
#     "-10.1", a negative real number
#     "1e5", a number in scientific notation
#     And here are examples of non-numbers:
#         "a"
#         "x 1"
#         "a -2"
#         "-"

# preamble: I will use the examples above to guide which types of numbers are acceptable,
# and particular treat fractions represented like 1/2 as not numbers. I will also
# treat 1e5e5 as not a number.

DIGITS = '0123456789'


def is_number(s):
    # the first e is accepted in between digits, and splits the string into two parts
    parts = s.split('e')
    if len(parts) == 1:
        return _is_valid_part(parts[0])
    elif len(parts) == 2 and all(parts):
        return _is_valid_part(parts[0]) and _is_valid_part(parts[1])
    else:
        return False


def _is_valid_part(s):
    # digits are accepted
    # the first . in each part is accepted in between digits
    is_negative = False
    has_digits = False
    decimal_index = 0
    for i, ch in enumerate(s):
        if ch not in DIGITS + '.-':
            return False  # only accept digits, decimal point and minus
        if ch == '.':
            if decimal_index:
                return False  # no double decimal point
            decimal_index = i
        if ch == '-':
            if i > 0:
                return False  # no minus after first character
            is_negative = True
        if not has_digits and ch in DIGITS:
            has_digits = True
    if not has_digits:
        return False
    if decimal_index and not _is_valid_decimal(s, decimal_index):
        return False
    return True


def _is_valid_decimal(s, decimal_index):
    try:
        decimal_between_digits = (s[decimal_index - 1] in DIGITS and
                                  s[decimal_index + 1] in DIGITS)
    except KeyError:
        return False  # no decimal as first or last character
    if not decimal_between_digits:
        return False  # decimal must be sandwiched by digits
    return True