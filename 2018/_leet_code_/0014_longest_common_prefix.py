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
    head = node
    previous = None

    idx = 0
    while node and idx < len(s):
        if node.val == s[idx]:
            previous = node
            node = node.next
            idx += 1
        else:
            break
    if previous:
        previous.next = None
    else:
        head = None
    return head


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        node = ll_from_str(strs[0])
        for i in range(1, len(strs)):
            node = trim_to_common(node, strs[i])

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
        self.assertEqual(
            "", s.longestCommonPrefix(["flower","flow","flight", "a"]))
        self.assertEqual(
            "", s.longestCommonPrefix(["dog","racecar","car"]))
        self.assertEqual(
            "", s.longestCommonPrefix([]))
        self.assertEqual(
            "dog", s.longestCommonPrefix(["dog"]))
        self.assertEqual(
            "dog", s.longestCommonPrefix(["dog", "dog", "dog"]))
        self.assertEqual(
            "a", s.longestCommonPrefix(["aa", "a"]))


if __name__ == "__main__":
    unittest.main()