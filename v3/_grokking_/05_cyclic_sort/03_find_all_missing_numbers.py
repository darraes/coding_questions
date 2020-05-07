def find_missing_numbers(nums):
    missingNumbers = []
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[j], nums[i] = nums[i], nums[j]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            missingNumbers.append(i + 1)

    return missingNumbers


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual([4, 6, 7], find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
        self.assertEqual([3], find_missing_numbers([2, 4, 1, 2]))
        self.assertEqual([1, 3], find_missing_numbers([2, 4, 2, 2]))


if __name__ == "__main__":
    unittest.main()
