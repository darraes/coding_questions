class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    total = 0

    def go(root, path_sum):
        nonlocal total

        if root is None:
            return

        path_sum *= 10
        path_sum += root.val

        if root.left is None and root.right is None:
            total += path_sum

        go(root.left, path_sum)
        go(root.right, path_sum)

    go(root, 0)
    return total


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
