def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual([1, 2, 3, 4, 5], cyclic_sort([3, 1, 5, 4, 2]))
        self.assertEqual([1, 2, 3, 4, 5, 6], cyclic_sort([2, 6, 4, 3, 1, 5]))
        self.assertEqual([1, 2, 3, 4, 5, 6], cyclic_sort([1, 5, 6, 4, 3, 2]))


if __name__ == "__main__":
    unittest.main()
