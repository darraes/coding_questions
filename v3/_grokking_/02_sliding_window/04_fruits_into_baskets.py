def fruits_into_baskets(fruits):
    window = {}

    def add_to_window(char):
        nonlocal window
        if char not in window:
            window[char] = 0
        window[char] += 1

    def del_from_window(char):
        nonlocal window
        window[char] -= 1
        if window[char] == 0:
            del window[char]

    K = 2
    max_length = window_start = 0
    for window_end in range(len(fruits)):
        add_to_window(fruits[window_end])

        while len(window) > K:
            del_from_window(fruits[window_start])
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length

###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))
        self.assertEqual(5, fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))


if __name__ == "__main__":
    unittest.main()