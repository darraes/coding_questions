def length_of_longest_substring(arr, k):
    max_length = max_repeated = number_of_1s = window_start = 0

    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            number_of_1s += 1

        window_length = window_end - window_start + 1

        if window_length - k > number_of_1s:
            if arr[window_start] == 1:
                number_of_1s -= 1
            window_start += 1
        else:
            max_length = max(max_length, window_length)

    return max_length


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            6, length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2)
        )
        self.assertEqual(
            9, length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3)
        )
        


if __name__ == "__main__":
    unittest.main()
