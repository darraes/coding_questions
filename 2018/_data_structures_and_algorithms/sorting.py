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


def quick_select(array, k):
    def swap(array, i, j):
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp

    mid = int(len(array) / 2)
    swap(array, mid, -1)
    pivot = array[-1]

    c = p = 0
    while p < len(array):
        if array[p] < pivot:
            swap(array, c, p)
            c += 1
        p += 1

    swap(array, c, -1)

    if c == k - 1:
        return array[k - 1]
    elif c > k - 1:
        return quick_select(array[:c], k)
    else:
        return quick_select(array[c:], k - c)


def quicksort(array, i, j):
    pass


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_mergesort(self):
        array = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        shuffle(array)
        self.assertEqual([11, 12, 13, 14, 15, 16, 17, 18, 19, 20], merge_sort(array))

    def test_quickselect(self):
        array = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        shuffle(array)
        self.assertEqual(17, quick_select(array, 7))
        self.assertEqual(11, quick_select(array, 1))
        self.assertEqual(20, quick_select(array, 10))

        array = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
        shuffle(array)
        self.assertEqual(17, quick_select(array, 7))
        self.assertEqual(11, quick_select(array, 1))
        self.assertEqual(20, quick_select(array, 10))
        self.assertEqual(21, quick_select(array, 11))


if __name__ == "__main__":
    unittest.main()
