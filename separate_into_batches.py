# Task: Separate a list of elements, returning a 2d list with the inner lists having a specified length.


def separate_into_batches(ls, batch_size):
    ls_2d = []
    batch = 1
    while batch < len(ls) // batch_size + 2:
        start = (batch - 1) * batch_size
        end = batch * batch_size
        ls_2d.append(ls[start:end])
        batch += 1
    return ls_2d
