from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
    is_next = False
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        node = queue.popleft()

        if node.val == key:
            is_next = True
        elif is_next:
            return node
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  result = find_successor(root, 12)
  if result:
    print(result.val)
  result = find_successor(root, 9)
  if result:
    print(result.val)


main()
