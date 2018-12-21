# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 == None or t2 == None:
            return False
        return (
            t1.val == t2.val
            and self.isMirror(t1.right, t2.left)
            and self.isMirror(t1.left, t2.right)
        )


###############################################################
import unittest

def build(array):
    idx = 0

    def _build(array):
        nonlocal idx
        node = None
        if idx < len(array) and array[idx] is not None:
            node = TreeNode(array[idx])
            idx += 1
            node.left = _build(array)
            node.right = _build(array)
            return node
        else:
            idx += 1
            return None

    root =  _build(array)
    return root

class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(False, s.isSymmetric(build([2, 1, None, None, 3])))
        self.assertEqual(False, s.isSymmetric(build([5, 1, 4, None, None, 3, 6])))
        self.assertEqual(
            True,
            s.isSymmetric(
                build(
                    [
                        1,
                        2,
                        3,
                        None,
                        None,
                        4,
                        None,
                        None,
                        2,
                        4,
                        None,
                        None,
                        3,
                        None,
                        None,
                    ]
                )
            ),
        )
        self.assertEqual(
            False,
            s.isSymmetric(build([1, 2, None, 3, None, None, 2, None, 3, None, None])),
        )
        self.assertEqual(False, s.isSymmetric(build([1, 2, 3, 3, None, 2, None])))


if __name__ == "__main__":
    unittest.main()
