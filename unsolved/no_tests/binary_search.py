from random import randint

array = []
array_length = 1000

number = 1
for i in range(array_length):
    array.append(number)
    number += randint(1, 30)

# now we should have a nice sorted array of randomish numbers

target_index = randint(0, array_length - 1)
target = array[target_index]
cycles = 1


def binary_search(ls, target, cycles=0):
    cycles += 1
    guess_index = len(ls) // 2
    val = ls[guess_index]
    print(f'guessing index {guess_index} and value {val}')
    if val == target:
        print(f'target found in {cycles} cycles')
    elif val > target:
        binary_search(ls[:guess_index], target=target, cycles=cycles)
    else:
        start = guess_index
        binary_search(ls[guess_index:], target=target, cycles=cycles)


print(f'target index is {target_index} target is {target}')
binary_search(array, target)

# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17