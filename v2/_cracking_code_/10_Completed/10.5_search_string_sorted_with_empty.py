def closest_non_empty(array, i, s, e):
    l = i - 1
    r = i + 1

    while True:
        if l < s and r > e:
            return -1
        if l >= s and array[l] != "":
            return l
        if r <= e and array[r] != "":
            return r

        l -= 1
        r += 1


def search(s, array):
    i, j = 0, len(array) - 1
    while i <= j:
        mid = (i + j) // 2
        # print(i, mid, j)

        if array[mid] == "":
            mid = closest_non_empty(array, mid, i, j)

        if mid == -1:
            return None
        # print(i, mid, j)

        if array[mid] == s:
            return mid
        elif s < array[mid]:
            j = mid - 1
        else:
            i = mid + 1

    return None


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, search("aa", ["aa", "", "", "da"]))
        self.assertEqual(0, search("aa", ["aa", "ba", "ca", "da"]))
        self.assertEqual(3, search("da", ["aa", "", "", "da"]))
        self.assertEqual(3, search("da", ["aa", "ba", "ca", "da"]))
        self.assertEqual(0, search("aa", ["aa", "", "", "", "", "da"]))
        self.assertEqual(2, search("ba", ["aa", "", "ba", "", "", "da"]))
        self.assertEqual(None, search("ab", ["aa", "", "ba", "", "", "da"]))
        self.assertEqual(None, search("f", ["aa", "", "ba", "", "", "da"]))
        self.assertEqual(None, search("bb", ["aa", "", "ba", "", "", "da"]))
        self.assertEqual(None, search("aa", ["", "", "", "", "", ""]))


if __name__ == "__main__":
    unittest.main()
