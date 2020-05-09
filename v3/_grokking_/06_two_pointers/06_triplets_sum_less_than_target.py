def triplet_with_smaller_sum(arr, target):
    count = 0
    arr = sorted(arr)

    for x in range(len(arr) - 2):
        y, z = x + 1, len(arr) - 1
        while y < z:
            cur_sum = arr[x] + arr[y] + arr[z]
            if cur_sum < target:
                count += z - y
                y  += 1
            else:
                z -= 1
    return count


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2, triplet_with_smaller_sum([-1, 0, 2, 3], target=3))
        self.assertEqual(4, triplet_with_smaller_sum([-1, 4, 2, 1, 3], target=5))


if __name__ == "__main__":
    unittest.main()
