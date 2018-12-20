class TreeNode:

    def __init__(self, left, right, value):
        self._left = left
        self._right = right
        self._value = value

"""Only works with trees of unique values"""
class TreeBuilder:

    """Recursion to rebuild the tree"""
    def build_tree(self, pre_order, in_order):
        self.pre_index = 0
        self.indexes = [0]*256
        for i in range(len(in_order)):
            self.indexes[in_order[i]] = i

        return self._build_tree(pre_order, in_order, 0, len(pre_order) - 1)


    """Recursion to rebuild the tree. This method is private."""
    def _build_tree(self, pre_order, in_order, in_start, in_end):
        if in_start > in_end: 
            return None

        node = TreeNode(None, None, pre_order[self.pre_index])
        self.pre_index += 1

        if in_start == in_end: return node

        in_index = self.indexes[node._value]

        node._left = self._build_tree(pre_order, in_order, in_start, in_index - 1)
        node._right = self._build_tree(pre_order, in_order, in_index + 1, in_end)

        return node

builder = TreeBuilder()
n = builder.build_tree([7,10,4,3,1,2,8,11], [4,10,3,1,7,11,8,2])