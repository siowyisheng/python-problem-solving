# Implement division of two positive integers without using the division,
# multiplication, or modulus operators. Return the quotient as an integer,
# ignoring the remainder.


def difficult_division(number, divisor):
    quotient = 0
    while number >= 0:
        number -= divisor
        quotient += 1
    return quotient