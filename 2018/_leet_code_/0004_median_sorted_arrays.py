def _median(l1, l2):
    target = int((len(l1) + len(l2)) / 2) + 1

    k = int(len(l2) / 2)
    i2 = k
    i1 = target - i2

    def found_check(l_a, i_a, l_b, i_b):
        return i_a > 0 and i_a <= len(l_a) \
            and (
                (i_b == 0 and l_a[i_a - 1] <= l_b[i_b])
                or (i_b == len(l_b) and l_a[i_a - 1] >= l_b[i_b - 1])
                or (l_a[i_a - 1] >= l_b[i_b - 1] and l_a[i_a - 1] <= l_b[i_b])
            )

    while True:
        print(i1, i2, k)
        found_in_1 = found_check(l1, i1, l2, i2)
        found_in_2 = found_check(l2, i2, l1, i1)


        if found_in_1 or found_in_2:
            break

        if l1[i1 - 1] > l2[i2]:
            delta = min(k, len(l2) - k, i1)
            i2 += delta
            i1 -= delta
        else:
            delta = min(k, len(l1) - k, i2)
            i1 += delta
            i2 -= delta

        
        k = max(1, int(k / 2))

    if found_in_1:
        return l1[i1 - 1]
    else:
        return l2[i2 - 1]


def median(l1, l2):
    if len(l1) >= len(l2):
        return _median(l1, l2)
    else:
        return _median(l2, l1)


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        #self.assertEqual(2, median([1, 3], [2]))
        #self.assertEqual(3, median([2, 4, 5], [1, 3]))
        #self.assertEqual(3, median([1, 3], [2, 4, 5]))
        #self.assertEqual(4, median([2, 3, 4, 5], [1, 6, 7]))
        self.assertEqual(6, median([1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11]))
        self.assertEqual(6, median([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11]))
        self.assertEqual(6, median([1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11]))
        self.assertEqual(6, median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]))


if __name__ == '__main__':
    unittest.main()