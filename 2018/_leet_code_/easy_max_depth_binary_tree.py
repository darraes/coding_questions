

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1




####### =============== TESTS =============== 
import unittest

class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def build_from_pre(list, cur_idx):
    if list[cur_idx[0]] is None:
        return None

    root = TreeNode(list[cur_idx[0]])
    cur_idx[0] += 1

    root.left = build_from_pre(list, cur_idx)
    root.right = build_from_pre(list, cur_idx)

    return root


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(
            3, s.maxDepth(build_from_pre([3,9,20,None,None,15,7], [0])))
        self.assertEqual(
            1, s.maxDepth(build_from_pre([20,None,None], [0])))
        self.assertEqual(
            0, s.maxDepth(build_from_pre([None], [0])))


if __name__ == '__main__':
    unittest.main()