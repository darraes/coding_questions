import random

def shuffle(array):
    for i in range(len(array)):
        source_i = random.randint(0, (len(array) - 1) - i) + i
        tmp = array[source_i]
        array[source_i] = array[i]
        array[i] = tmp
    return array


print shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])