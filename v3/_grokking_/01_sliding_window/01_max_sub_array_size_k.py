def max_sub_array_of_size_k(k, arr):
    max_sum = cur_sum = w_start = 0

    for w_end in range(len(arr)):
        cur_sum += arr[w_end]

        if w_end >= k - 1:
            max_sum = max(max_sum, cur_sum)
            cur_sum -= arr[w_start]
            w_start += 1

    return max_sum


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEquals(9, max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))
        self.assertEquals(7, max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))


if __name__ == "__main__":
    unittest.main()