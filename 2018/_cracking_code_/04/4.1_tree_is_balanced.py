from tree_utils import TreeNode, pretty_print, friendly_build, tree_equals

def is_balanced_impl(root):
    if root is None:
        return 0

    l_height = is_balanced_impl(root.left)
    if l_height == -1:
        return -1  # Not balanced
    
    r_height = is_balanced_impl(root.right)
    if r_height == -1:
        return -1  # Not balanced

    if abs(r_height - l_height) > 1:
        return -1  # Not balanced
                   
    return max(r_height, l_height) + 1


def is_balanced(root):
    return is_balanced_impl(root) != -1


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        root = friendly_build([["1"],
                               ["2", "3"],
                               ["4", "5", "6", "7"],
                               ["8", "9", "10", "11", "12", "13", "14", "15"]])
        self.assertTrue(is_balanced(root))

        root = friendly_build([["1"],
                               ["2", "3"],
                               ["4", "5", "N", "N"],
                               ["8", "9", "10", "11"]])
        self.assertFalse(is_balanced(root))

        root = friendly_build([["1"],
                               ["2", "3"],
                               ["4", "N", "6", "7"],
                               ["8", "9", "12", "13", "14", "15"]])
        self.assertFalse(is_balanced(root))




if __name__ == '__main__':
    unittest.main()