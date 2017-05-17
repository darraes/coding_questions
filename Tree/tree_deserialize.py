from collections import deque

class TreeNode:
    _left = None
    _right = None
    _value = 0

    def __init__(self, left, right, value):
        self._left = left
        self._right = right
        self._value = value

def serialize(node):
    result = "{} ".format(node._value)

    if node._left is None: result = result + "N "
    else: result = result + serialize(node._left)

    if node._right is None: result = result + "N "
    else: result = result + serialize(node._right)

    return result

def deserialize_word(tokens):
    token = tokens.popleft()

    if token == "N": return None
    else:
        return TreeNode(deserialize_word(tokens)
                        , deserialize_word(tokens)
                        , int(token))

def deserialize(phrase):
    tokens = deque()
    for word in phrase.split():
        tokens.append(word)

    return deserialize_word(tokens)


root = TreeNode(TreeNode(TreeNode(None, None, 49), None, 112), TreeNode(TreeNode(None, TreeNode(None, None, 5), 34), TreeNode(None, None, 16), 78), 4)
print serialize(root)
print serialize(deserialize(serialize(root)))