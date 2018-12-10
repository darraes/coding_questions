from tree_utils import TNode, pretty_print, friendly_build, tree_equals


def build(array):
    def _build(array, i, j):
        if i > j:
            return None

        mid = int((i + j) / 2)

        node = TNode(array[mid])
        node.left = _build(array, i, mid - 1)
        node.right = _build(array, mid + 1, j)

        return node
    return _build(array, 0, len(array) - 1)


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        root = friendly_build([["4"], ["2", "6"], ["1", "3", "5", "7"]])
        tree = build([1, 2, 3, 4, 5, 6, 7])
        pretty_print(tree)
        pretty_print(root)
        self.assertTrue(tree_equals(root, tree))


if __name__ == "__main__":
    unittest.main()
