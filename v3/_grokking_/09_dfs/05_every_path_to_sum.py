class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    def go(root, S, current_path):
        if root is None:
            return 0

        current_path.append(root.val)
        count_ending_here = 0
        tmp_path_sum = 0
        for i in range(len(current_path) - 1, -1, -1):
            tmp_path_sum += current_path[i]
            if tmp_path_sum == S:
                count_ending_here += 1

        count_ending_here += go(root.left, S, current_path) + go(
            root.right, S, current_path
        )
        del current_path[-1]
        return count_ending_here

    return go(root, S, [])


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
