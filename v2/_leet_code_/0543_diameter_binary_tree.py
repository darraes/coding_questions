class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0

        def height(node):
            nonlocal ans
            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)
            ans = max(ans, left_height + right_height + 1)
            return max(left_height, right_height) + 1

        if not root:
            return 0

        height(root)
        return ans - 1


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()


if __name__ == "__main__":
    unittest.main()
