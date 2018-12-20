# http://www.careercup.com/question?id=5214848900136960

class TreeNode:
    def __init__(self, left, right, value):
        self._left = left
        self._right = right
        self._value = value
        self._onLeft = 0

def _place(node, value, smallerAbove):
    if value >= node._value:
        if node._right == None:
            node._right = TreeNode(None, None, value)
            return smallerAbove + 1
        else:
            return _place(node._right, value, smallerAbove + node._onLeft + 1)
    else:
        node._onLeft += 1
        if node._left == None:
            node._left = TreeNode(None, None, value)
            return smallerAbove
        else:
           return _place(node._left, value, smallerAbove)

def solve(data):
    result = [0]*len(data)
    index = len(data) - 2
    root = TreeNode(None, None, data[index + 1])
    while index >= 0:
        result[index] = _place(root, data[index], 0)
        index -= 1
    return result

print solve([1,3,2,4,5,4,2])