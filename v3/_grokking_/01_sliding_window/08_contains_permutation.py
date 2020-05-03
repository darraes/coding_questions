def find_permutation(str, pattern):
    window = {}
    target = {}

    def add_to_window(index, char):
        if char not in index:
            index[char] = 0
        index[char] += 1

    def del_from_window(index, char):
        index[char] -= 1
        if index[char] == 0:
            del index[char]

    for c in pattern:
        add_to_window(target, c)

    window_start = 0
    for window_end in range(len(str)):
        add_to_window(window, str[window_end])

        if window_end < len(pattern) - 1:
            continue

        if window == target:
            return True

        del_from_window(window, str[window_start])
        window_start += 1

    return False

###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(False, find_permutation("odicf", "dc"))
        self.assertEqual(True, find_permutation("bcdxabcdy", "bcdyabcdx"))
        self.assertEqual(True, find_permutation("aaacb", "abc"))


if __name__ == "__main__":
    unittest.main()