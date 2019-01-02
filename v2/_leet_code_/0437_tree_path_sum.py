class Solution:
    def pathSum(self, root, target_sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        ans = 0

        def navigate(node, path):
            nonlocal ans, target_sum

            if node is None:
                return

            path.append(node)

            cur_sum = 0
            for i in range(len(path) - 1, -1, -1):
                cur_sum += path[i].val
                if cur_sum == target_sum:
                    ans += 1

            navigate(node.left, path)
            navigate(node.right, path)

            del path[-1]

        navigate(root, [])
        return ans


###############################################################
import unittest
from tree_utils import pretty_print, serialize, deserialize


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        problem = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
        self.assertEqual(3, s.pathSum(deserialize(problem), 8))

        problem = [10]
        self.assertEqual(1, s.pathSum(deserialize(problem), 10))

        problem = [10]
        self.assertEqual(0, s.pathSum(deserialize(problem), 9))

        problem = []
        self.assertEqual(0, s.pathSum(deserialize(problem), 9))


if __name__ == "__main__":
    unittest.main()
