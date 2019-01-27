from collections import deque
from tree_utils import TreeNode, pretty_print, friendly_build, tree_equals


def level_lists(root):
    ans = []
    queue = deque([(root, 0)])
    while len(queue) > 0:
        cur = queue.popleft()
        if not cur[0]:
            continue

        if cur[1] >= len(ans):
            ans.append([])
        ans[cur[1]].append(cur[0])

        queue.append((cur[0].left, cur[1] + 1))
        queue.append((cur[0].right, cur[1] + 1))

    return ans


###############################################################
import unittest


def print_lists(lists):
    for l in lists:
        print([n.value for n in l])


class TestFunctions(unittest.TestCase):
    def test_1(self):
        root = friendly_build(
            [
                ["1"],
                ["2", "3"],
                ["4", "5", "6", "7"],
                ["8", "9", "10", "11", "12", "13", "14", "15"],
            ]
        )
        lists = level_lists(root)
        print_lists(lists)

        root = friendly_build(
            [["1"], ["2", "3"], ["4", "5", "N", "N"], ["8", "9", "10", "11"]]
        )
        lists = level_lists(root)
        print_lists(lists)

        root = friendly_build(
            [
                ["1"],
                ["2", "3"],
                ["4", "N", "6", "7"],
                ["8", "9", "12", "13", "14", "15"],
            ]
        )
        lists = level_lists(root)
        print_lists(lists)


if __name__ == "__main__":
    unittest.main()
