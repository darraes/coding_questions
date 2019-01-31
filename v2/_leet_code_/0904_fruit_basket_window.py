class Solution:
    def totalFruit(self, tree):
        def before(window):
            min_k = min_v = None
            for k, v in window.items():
                if min_v is None or v < min_v:
                    min_k, min_v = k, v

            return min_k, min_v

        window = {}
        start = max_window_length = 0
        for i in range(len(tree)):
            window[tree[i]] = i

            if len(window) == 3:
                min_k, min_v = before(window)
                start = min_v + 1
                del window[min_k]
            max_window_length = max(max_window_length, i - start + 1)

        return max_window_length


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertEqual(3, s.totalFruit([0, 1, 2, 2]))
        self.assertEqual(4, s.totalFruit([1, 2, 3, 2, 2]))
        self.assertEqual(5, s.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
        self.assertEqual(4, s.totalFruit([3, 3, 3, 1, 4, 5, 1, 4, 5, 1]))
        self.assertEqual(3, s.totalFruit([1, 2, 1]))


if __name__ == "__main__":
    unittest.main()
