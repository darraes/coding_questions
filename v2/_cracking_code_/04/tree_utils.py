from collections import deque


class TreeNode:
    def __init__(self, left, right, value):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None

def tnode(value, left = None, right = None):
    return TreeNode(left, right, value)

# Calculates the depth of the tree
def depth(node):
    if node is None:
        return 0
    else:
        return max(depth(node.left), depth(node.right)) + 1


# Compares 2 TreeNodes for equality
def tree_equals(node1, node2):
    if not node1 and not node2:
        return True

    if (node1 and not node2) or (node2 and not node1) or node1.value != node2.value:
        print(node1.value, node2.value)
        return False

    return tree_equals(node1.left, node2.left) and tree_equals(node1.right, node2.right)


# Transforms a list of lists that represents the nodes into a Tree
# This:
# [["1"],
#  ["2", "3"],
#  ["4", "5", "6", "7"],
#  ["8", "9", "0", "11", "8", "9", "0", "1"]]
#
#  Becomes:
#         1
#    2        3
#  4   5    6   7
# 8 9 0 11 8 9 0 1
#
def friendly_build(lines):
    def build_node(value):
        if value == "N":
            return None
        return TreeNode(None, None, int(value))

    parents = deque()
    children = deque()
    children.append(build_node(lines[0][0]))
    root = None

    for i in range(len(lines)):
        j = 0
        while len(parents) > 0:
            current_parent = parents.popleft()
            if root is None:
                root = current_parent

            current_parent.left = build_node(lines[i][j])
            if current_parent.left:
                current_parent.left.parent = current_parent
            j += 1
            current_parent.right = build_node(lines[i][j])
            if current_parent.right:
                current_parent.right.parent = current_parent
            j += 1

            if current_parent.left:
                children.append(current_parent.left)
            if current_parent.right:
                children.append(current_parent.right)

        if i != 0 and j != len(lines[i]):
            raise

        parents = children
        children = deque()

    return root


#  Prints a tree honoring spaces for a better visualization
#
#         1
#    2        3
#  4   5    6   7
# 8 9 0 11 8 9 0 1
def pretty_print(node):
    def add_to(writer, dep, pos, c):
        value = str(c)
        line = writer[dep]

        for i in range(pos - len(line)):
            line.append(" ")

        line.extend(list(value))
        return len(value)

    def impl(node, c_depth, c_pos, writer):
        if not node:
            return c_pos

        c_pos = impl(node.left, c_depth + 1, c_pos, writer)

        c_pos += add_to(writer, c_depth, c_pos, node.value)

        c_pos = impl(node.right, c_depth + 1, c_pos, writer)
        return c_pos

    writer = []
    for x in range(depth(node)):
        writer.append([])

    impl(node, 0, 0, writer)

    for l in writer:
        print("".join(l))
