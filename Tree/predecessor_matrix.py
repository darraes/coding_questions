# http://www.careercup.com/question?id=5666998226780160

class TreeNode:

    def __init__(self, left, right, value):
        self._left = left
        self._right = right
        self._value = value

    
def inheritance_indexes(indexes, node, parentIndex, lastIndex):
    if node == None:
        return lastIndex

    nodeIndex = lastIndex + 1
    indexes.append((node._value, nodeIndex, parentIndex))

    lastIndex = inheritance_indexes(indexes, node._left, nodeIndex, nodeIndex)
    lastIndex = inheritance_indexes(indexes, node._right, nodeIndex, lastIndex)

    return lastIndex

def inheritance_matrix(matrix, node, ancestors, lastIndex):
    if node == None:
        return lastIndex

    nodeIndex = lastIndex + 1
    for a in ancestors:
        matrix[a][nodeIndex] = 1

    ancestors.append(nodeIndex)
    lastIndex = inheritance_matrix(matrix, node._left, ancestors, nodeIndex)
    lastIndex = inheritance_matrix(matrix, node._right, ancestors, lastIndex)
    ancestors.pop()

    return lastIndex

root = TreeNode(TreeNode(TreeNode(None, None, 49), None, 112), TreeNode(TreeNode(None, TreeNode(None, None, 5), 34), TreeNode(None, None, 16), 78), 4)
chain = []
inheritance_indexes(chain, root, -1, -1)
print chain

matrix = [[0 for x in xrange(7)] for x in xrange(7)] 
inheritance_matrix(matrix, root, [], -1)
for row in matrix:
    print row

