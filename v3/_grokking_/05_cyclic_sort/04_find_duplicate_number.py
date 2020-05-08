def find_duplicate(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != i + 1:
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i]
        else:
            i += 1
    return -1


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(4, find_duplicate([1, 4, 4, 3, 2]))
        self.assertEqual(3, find_duplicate([2, 1, 3, 3, 5, 4]))
        self.assertEqual(4, find_duplicate([2, 4, 1, 4, 4]))


if __name__ == "__main__":
    unittest.main()
