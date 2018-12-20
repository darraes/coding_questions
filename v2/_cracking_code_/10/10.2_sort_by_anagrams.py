def sort(words):
    def compare(w1):
        return "".join(sorted(list(w1)))

    words.sort(key=compare)
    return words


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEquals(['daniel', 'nielda', 'bc', 'cb', 'zs'],
                          sort(["zs", "bc", "cb", "daniel", "nielda"]))


if __name__ == '__main__':
    unittest.main()