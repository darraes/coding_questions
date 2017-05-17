# http://www.careercup.com/question?id=5182821194792960

def front_non_zeros(array):
    i = 0
    end = len(array) - 1

    while i < end:
        while i < len(array):
            if array[i] == 0: break
            else: i += 1

        while end >= 0:
            if array[end] != 0: break
            else: end -= 1

        if (i < end):
            swap = array[i]
            array[i] = array[end]
            array[end] = swap

            i += 1
            end -= 1

    return (end + 1, array)

print front_non_zeros([1, 0, 2, 0, 0, 3, 4, 3, 0, 9])