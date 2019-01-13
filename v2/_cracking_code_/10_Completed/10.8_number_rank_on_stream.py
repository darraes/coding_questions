class TreeNode:
    def __init__(self, val):
        self.val = val
        self.lcount = 0
        self.left = None
        self.right = None


class Tracker:
    def __init__(self):
        self.root = None

    def track(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return

        node = self.root

        while True:
            if val <= node.val:
                node.lcount += 1
                if not node.left:
                    node.left = TreeNode(val)
                    break
                node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                node = node.right

    def rank(self, val):
        node = self.root
        smaller = 0
        while node:
            if val == node.val:
                return smaller
            if val < node.val:
                node = node.left
            else:
                smaller += node.lcount + 1
                node = node.right

        return -1

    def print(self):
        def in_order(node):
            if not node:
                return

            in_order(node.left)
            print(node.lcount, node.val)
            in_order(node.right)

        in_order(self.root)


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        tracker = Tracker()
        tracker.track(10)
        tracker.track(15)
        tracker.track(5)
        tracker.track(2)
        tracker.track(4)
        tracker.track(18)
        tracker.track(17)
        tracker.track(20)

        self.assertEqual(4, tracker.rank(15))
        self.assertEqual(0, tracker.rank(2))
        self.assertEqual(7, tracker.rank(20))


if __name__ == "__main__":
    unittest.main()
