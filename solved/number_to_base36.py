# Task: Take a positive integer and output a base-36 string.


def to_b36(num):
    num_to_b36 = {
        num: chr(ord) for num, ord in zip(
            list(range(1, 37)),
            list(range(48, 58)) + list(range(97, 123)))
    }
    values = []
    values.append(num % 36)
    while num // 36 > 0:
        num = num // 36
        values.append(num % 36)

    s = ''
    for value in values:
        s += num_to_b36[value]
    return s
