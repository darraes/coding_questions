class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def ll_from_str(s):
    head = node = None
    for i in range(len(s)):
        cur = Node(s[i])
        if not node:
            head = node = cur
        else:
            node.next = cur
            node = node.next
    return head


def trim_to_common(node, s):
    previous = None

    idx = 0
    while node and idx < len(s):
        if node.val == s[idx]:
            previous = node
            node = node.next
            idx += 1
        else:
            if previous:
                previous.next = None
            break


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        node = ll_from_str(strs[0])
        for i in range(1, len(strs)):
            trim_to_common(node, strs[i])

        if not node:
            return ""

        prefix = []
        while node:
            prefix.append(node.val)
            node = node.next
        return "".join(prefix)



####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(
            "fl", s.longestCommonPrefix(["flower","flow","flight"]))


if __name__ == "__main__":
    unittest.main()