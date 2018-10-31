# https://code.google.com/p/prep/wiki/ExercisesList

# Calculate the depth of a binary tree (for practical reasons, assume a tree with a single element has depth = 1).

from collections import deque

class TreeNode:
    def __init__(self, left, right, value):
        self._left = left
        self._right = right
        self._value = value

    @staticmethod
    def max_depth_nr(node):
        queue = deque()
        queue.append((node, 1))
        max_height = 0

        while len(queue) > 0:
            n, h = queue.popleft();

            if max_height < h: max_height = h

            if n._left is not None:
                queue.append((n._left, h + 1))
            if n._right is not None:
                queue.append((n._right, h + 1))

        return max_height


root = TreeNode(TreeNode(TreeNode(None, None, 49), None, 112), TreeNode(TreeNode(None, TreeNode(TreeNode(None, None, 5), None, 5), 34), TreeNode(None, None, 16), 78), 4)
print TreeNode.max_depth_nr(root)