class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    allPaths = []

    def find(root, sum, path):
        nonlocal allPaths

        if root is None:
            return

        path.append(root.val)

        if sum == root.val and root.left is None and root.right is None:
            allPaths.append(list(path))

        find(root.left, sum - root.val, path)
        find(root.right, sum - root.val, path)

        del path[-1]

    find(root, sum, [])
    return allPaths


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) + ": " + str(find_paths(root, sum)))


main()
