from tree_utils import TreeNode, pretty_print, friendly_build, tree_equals


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        root = friendly_build([["1"],
                               ["2", "3"],
                               ["4", "5", "6", "7"],
                               ["8", "9", "10", "11", "12", "13", "14", "15"]])
        pretty_print(root)


if __name__ == '__main__':
    unittest.main()