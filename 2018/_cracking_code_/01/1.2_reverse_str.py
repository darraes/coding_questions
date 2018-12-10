def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def reverse(istr):
    chars = list(istr)

    i = 0
    j = len(chars) - 1

    while i < j:
        swap(chars, i, j)
        i += 1
        j -= 1

    return "".join(chars)


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual("leinad", reverse("daniel"))
        self.assertEqual("aleinad", reverse("daniela"))
        self.assertEqual("a", reverse("a"))


if __name__ == '__main__':
    unittest.main()