import math

def smallest_subarray_with_given_sum(s, arr):
    min_length = math.inf
    cur_sum = window_start = window_end = 0

    while window_end < len(arr):
        cur_sum += arr[window_end]
        
        while cur_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            cur_sum -= arr[window_start]
            window_start += 1

        window_end += 1

    return min_length if min_length < math.inf else 0


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEquals(2, smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))
        self.assertEquals(1, smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]))


if __name__ == "__main__":
    unittest.main()
