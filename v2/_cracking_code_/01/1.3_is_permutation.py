def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    counter = {}

    for letter in s1:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1

    for letter in s2:
        if letter not in counter:
            return False
        counter[letter] -= 1
        if counter[letter] < 0:
            return False

    return True



###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_permutation("daniel", "nielda"))
        self.assertFalse(is_permutation("daniel", "nielei"))


if __name__ == '__main__':
    unittest.main()