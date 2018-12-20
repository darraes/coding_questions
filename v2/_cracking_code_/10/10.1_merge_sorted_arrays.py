def merge(large, l_length, small):
    index = l_length + len(small) - 1
    s_idx = len(small) - 1
    l_idx = l_length - 1

    while index >= 0:
        if s_idx == -1 or (l_idx >= 0 and large[l_idx] > small[s_idx]):
            large[index] = large[l_idx]
            l_idx -= 1
        else:
            large[index] = small[s_idx]
            s_idx -= 1
        index -= 1
    return large


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            [1, 2, 3, 4, 5], merge([1, 2, 3, None, None], 3, [4, 5]))


if __name__ == '__main__':
    unittest.main()