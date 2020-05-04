import math


def triplet_sum_close_to_target(arr, target_sum):
    closest = math.inf

    arr = sorted(arr)

    for x in range(len(arr) - 2):
        y, z = x + 1, len(arr) - 1
        while y < z:
            cur_sum = arr[x] + arr[y] + arr[z]
            if abs(target_sum - closest) > abs(target_sum - cur_sum):
                closest = cur_sum
            elif abs(target_sum - closest) == abs(target_sum - cur_sum):
                closest = min(cur_sum, closest)

            if cur_sum > target_sum:
                z -= 1
            elif cur_sum < target_sum:
                y += 1
            else:
                break
    return closest


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, triplet_sum_close_to_target([-2, 0, 1, 2], 2))
        self.assertEqual(0, triplet_sum_close_to_target([-3, -1, 1, 2], 1))
        self.assertEqual(3, triplet_sum_close_to_target([1, 0, 1, 1], 100))


if __name__ == "__main__":
    unittest.main()
