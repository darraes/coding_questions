def length_of_longest_substring(str, k):
    window = {}
    max_repeated = 0

    def add_to_window(char):
        nonlocal window, max_repeated
        if char not in window:
            window[char] = 0

        window[char] += 1
        max_repeated = max(max_repeated, window[char])

    def del_from_window(char):
        nonlocal window, max_repeated
        window[char] -= 1
        if window[char] == 0:
            del window[char]

    max_length = window_start = 0
    for window_end in range(len(str)):
        add_to_window(str[window_end])

        cur_length = window_end - window_start + 1
        if cur_length - max_repeated > k:
            del_from_window(str[window_start])
            window_start += 1

        cur_length = window_end - window_start + 1
        max_length = max(max_length, cur_length)

    return max_length

###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(5, length_of_longest_substring("aabccbb", 2))
        self.assertEqual(4, length_of_longest_substring("abbcb", 1))
        self.assertEqual(3, length_of_longest_substring("abccde", 1))


if __name__ == "__main__":
    unittest.main()