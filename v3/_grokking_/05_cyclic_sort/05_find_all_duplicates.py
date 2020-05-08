def find_all_duplicates(nums):
    duplicateNumbers = []
    i = 0

    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != i + 1:
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                duplicateNumbers.append(nums[i])
                i += 1
        else:
            i += 1

    return set(duplicateNumbers)

###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(set([4, 5]), find_all_duplicates([3, 4, 4, 5, 5]))
        self.assertEqual(set([3, 5]), find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


if __name__ == "__main__":
    unittest.main()