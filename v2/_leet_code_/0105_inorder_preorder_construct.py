# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        pre_i = 0
        lookup = {}
        for i, e in enumerate(inorder):
            lookup[e] = i

        def _build_from_in_pre(pre_order, in_order, in_s, in_e):
            nonlocal pre_i, lookup
            if in_s > in_e:
                return None

            node = TreeNode(pre_order[pre_i])
            pre_i += 1
            if in_s != in_e:
                node.left = _build_from_in_pre(
                    pre_order, in_order, in_s, lookup[node.val] - 1
                )
                node.right = _build_from_in_pre(
                    pre_order, in_order, lookup[node.val] + 1, in_e
                )
            return node

        return _build_from_in_pre(preorder, inorder, 0, len(inorder) - 1)