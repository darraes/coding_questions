from random import shuffle


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = int(len(array) / 2)
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    # Merging
    res = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        elif i < len(left):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    return res


def quicksort(array, i, j):
    pass


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        array = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        shuffle(array)
        self.assertEqual([11, 12, 13, 14, 15, 16, 17, 18, 19, 20], merge_sort(array))


if __name__ == "__main__":
    unittest.main()
