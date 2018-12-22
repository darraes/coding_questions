from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Calculates the depth of the tree
def depth(node):
    if node is None:
        return 0
    else:
        return max(depth(node.left), depth(node.right)) + 1


def pretty_print(node):
    def add_to(writer, dep, pos, c):
        val = str(c)
        line = writer[dep]

        for i in range(pos - len(line)):
            line.append(" ")

        line.extend(list(val))
        return len(val)

    def impl(node, c_depth, c_pos, writer):
        if not node:
            return c_pos

        c_pos = impl(node.left, c_depth + 1, c_pos, writer)

        c_pos += add_to(writer, c_depth, c_pos, node.val)

        c_pos = impl(node.right, c_depth + 1, c_pos, writer)
        return c_pos

    writer = []
    for x in range(depth(node)):
        writer.append([])

    impl(node, 0, 0, writer)

    for l in writer:
        print("".join(l))


def serialize(root):
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

def deserialize(data):
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
