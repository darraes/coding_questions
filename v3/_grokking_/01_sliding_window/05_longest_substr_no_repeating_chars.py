def non_repeat_substring(str):
    window = {}
    repeated_count = 0

    def add_to_window(char):
        nonlocal window, repeated_count
        if char not in window:
            window[char] = 0
        elif window[char] == 1:
            repeated_count += 1
        window[char] += 1

    def del_from_window(char):
        nonlocal window, repeated_count
        window[char] -= 1
        if window[char] == 0:
            del window[char]
        elif window[char] == 1:
            repeated_count -= 1

    max_length = window_start = 0

    for window_end in range(len(str)):
        add_to_window(str[window_end])

        while repeated_count > 0:
            del_from_window(str[window_start])
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def non_repeat_substring2(str):
    window = {}
    max_length = window_start = 0

    for window_end in range(len(str)):
        if str[window_end] in window:
            window_start = max(window_start, window[str[window_end]] + 1)

        window[str[window_end]] = window_end
        max_length = max(max_length, window_end - window_start + 1)

    return max_length

###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEquals(3, non_repeat_substring("aabccbb"))
        self.assertEquals(2, non_repeat_substring("abbbb"))
        self.assertEquals(3, non_repeat_substring("abccde"))

    def test_2(self):
        self.assertEquals(3, non_repeat_substring2("aabccbb"))
        self.assertEquals(2, non_repeat_substring2("abbbb"))
        self.assertEquals(3, non_repeat_substring2("abccde"))


if __name__ == "__main__":
    unittest.main()