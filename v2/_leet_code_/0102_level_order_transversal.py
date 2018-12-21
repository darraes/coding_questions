# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
            
        to_visit = deque([(root, 0)])
        answer = []

        while len(to_visit) > 0:
            node, level = to_visit.popleft()
            if level == len(answer):
                answer.append([])

            answer[level].append(node.val)

            if node.left:
                to_visit.append((node.left, level + 1))
            if node.right:
                to_visit.append((node.right, level + 1))

        return answer


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

    root = _build(array)
    return root


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(
            [[3], [9, 20], [15, 7]],
            s.levelOrder(build([3, 9, None, None, 20, 15, None, None, 7, None, None])),
        )

        self.assertEqual(
            [[3]],
            s.levelOrder(build([3])),
        )

        self.assertEqual(
            [],
            s.levelOrder(build([None])),
        )


if __name__ == "__main__":
    unittest.main()
