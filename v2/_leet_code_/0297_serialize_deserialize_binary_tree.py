# You may serialize the following tree:
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# as "[1,2,3,null,null,4,5]"


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        node = root
        queue = deque([node])

        while len(queue) > 0:
            current = queue.popleft()
            ans.append(current.val if current else None)

            if current:
                queue.append(current.left)
                queue.append(current.right)

        while len(ans) > 0 and ans[-1] is None:
            ans.pop()
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        producers = deque(data)
        p = producers.popleft()

        root = TreeNode(p)
        consumers = deque([root])

        while len(consumers) > 0:
            current = consumers.popleft()

            if len(producers) > 0:
                left = producers.popleft()
                current.left = TreeNode(left) if left is not None else None
                if current.left:
                    consumers.append(current.left)

            if len(producers) > 0:
                right = producers.popleft()
                current.right = TreeNode(right) if right is not None else None
                if current.right:
                    consumers.append(current.right)

        return root


###############################################################
import unittest
from tree_utils import pretty_print


class TestFunctions(unittest.TestCase):
    def test_1(self):
        codec = Codec()

        problem = [-10, 9, 20, None, None, 15, 7]
        self.assertEqual(problem, codec.serialize(codec.deserialize(problem)))

        problem = [-10]
        self.assertEqual(problem, codec.serialize(codec.deserialize(problem)))

        problem = []
        self.assertEqual(problem, codec.serialize(codec.deserialize(problem)))


if __name__ == "__main__":
    unittest.main()
