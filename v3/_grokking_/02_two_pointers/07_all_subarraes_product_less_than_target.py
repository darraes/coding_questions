from collections import deque 

def find_subarrays(arr, target):
    result = []

    left = 0
    cur_prod = 1
    for right in range(len(arr)):
        cur_prod *= arr[right]

        while cur_prod >= target and left < len(arr):
            cur_prod /= arr[left]
            left += 1

        tmp = deque()
        for i in range(right, left - 1, -1):
            tmp.appendleft(arr[i])
            result.append(list(tmp))

    return result


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            [[2], [5], [2, 5], [3], [5, 3], [10]],
            find_subarrays([2, 5, 3, 10], target=30),
        )


if __name__ == "__main__":
    unittest.main()
