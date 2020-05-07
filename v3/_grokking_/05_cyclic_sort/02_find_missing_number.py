def find_missing_number(nums):
    i = 0
    while i < len(nums):
        j = nums[i]
        if nums[i] < len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if i != nums[i]:
            return i

    return len(nums)


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2, find_missing_number([4, 0, 3, 1]))
        self.assertEqual(7, find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
        self.assertEqual(8, find_missing_number([7, 3, 5, 2, 4, 6, 0, 1]))


if __name__ == "__main__":
    unittest.main()
