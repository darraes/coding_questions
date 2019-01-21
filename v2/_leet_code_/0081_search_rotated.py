class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        i = 0
        j = len(nums) - 1

        def _search(s, e):
            nonlocal nums, target
            if s > e:
                return False
            
            mid = (s + e) // 2
            if nums[mid] == target:
                return True

            if nums[s] < nums[mid]:
                if nums[s] <= target < nums[mid]:
                    return _search(s, mid - 1)
                else:
                    return _search(mid + 1, e)
            elif nums[mid] < nums[e]:
                if nums[mid] < target <= nums[e]:
                    return _search(mid + 1, e)
                else:
                    return _search(s, mid - 1)
            else:
                return _search(mid + 1, e) or _search(s, mid - 1)

        return _search(i, j)


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertTrue(s.search(nums=[1, 3, 1, 1, 1], target=3))
        self.assertTrue(s.search(nums=[1, 1, 1, 3, 1], target=3))
        self.assertTrue(s.search(nums=[3, 1], target=1))
        self.assertTrue(s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=5))
        self.assertTrue(s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0))
        self.assertTrue(s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=1))
        self.assertTrue(s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=6))
        self.assertFalse(s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=3))
        self.assertFalse(s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=4))
        self.assertFalse(s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=7))


if __name__ == "__main__":
    unittest.main()
