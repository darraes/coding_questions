# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res, _ = self.is_palindrome(head, head)
        return res

    def is_palindrome(self, slow, fast):
        if slow is None or slow.next is None:
            return (True, None)
        if fast.next is None:
            return (True, slow.next)
        if fast.next.next is None:
            return (slow.val == slow.next.val, slow.next.next)

        res, cmp_node = self.is_palindrome(slow.next, fast.next.next)

        return res and slow.val == cmp_node.val, cmp_node.next


# 1->2->2->1
# 1->2->1->2->1
#
# ###############################################################
import unittest


def from_list(list):
    idx = 0
    while idx < len(list) - 1:
        list[idx].next = list[idx + 1]
        idx += 1
    return list[0]


class TestFunctions(unittest.TestCase):
    def test_positive(self):
        print("====================")
        s = Solution()
        head = from_list(
            [
                ListNode(1),
                ListNode(2),
                ListNode(3),
                ListNode(3),
                ListNode(2),
                ListNode(1),
            ]
        )
        self.assertTrue(s.isPalindrome(head))

        head = from_list(
            [
                ListNode(1),
                ListNode(2),
                ListNode(3),
                ListNode(2),
                ListNode(1),
            ]
        )
        self.assertTrue(s.isPalindrome(head))

        head = from_list(
            [
                ListNode(1),
                ListNode(2),
                ListNode(2),
                ListNode(1),
            ]
        )
        self.assertTrue(s.isPalindrome(head))

        head = from_list(
            [
                ListNode(1),
                ListNode(2),
                ListNode(1),
            ]
        )
        self.assertTrue(s.isPalindrome(head))

        head = from_list(
            [
                ListNode(1),
                ListNode(1),
            ]
        )
        self.assertTrue(s.isPalindrome(head))

        head = from_list(
            [
                ListNode(1),
            ]
        )
        self.assertTrue(s.isPalindrome(head))

    def test_negative(self):
        print("====================")
        s = Solution()
        head = from_list(
            [
                ListNode(1),
                ListNode(2),
                ListNode(3),
                ListNode(3),
                ListNode(4),
                ListNode(2),
                ListNode(1),
            ]
        )
        self.assertFalse(s.isPalindrome(head))

        head = from_list(
            [
                ListNode(1),
                ListNode(2),
                ListNode(3),
                ListNode(2),
                ListNode(4),
                ListNode(1),
            ]
        )
        self.assertFalse(s.isPalindrome(head))

        head = from_list(
            [
                ListNode(1),
                ListNode(4),
                ListNode(2),
                ListNode(2),
                ListNode(1),
            ]
        )
        self.assertFalse(s.isPalindrome(head))

        head = from_list(
            [
                ListNode(1),
                ListNode(2),
                ListNode(1),
                ListNode(4),
            ]
        )
        self.assertFalse(s.isPalindrome(head))

        head = from_list(
            [
                ListNode(4),
                ListNode(1),
                ListNode(1),
            ]
        )
        self.assertFalse(s.isPalindrome(head))

        head = from_list(
            [
                ListNode(1),
                ListNode(4),
            ]
        )
        self.assertFalse(s.isPalindrome(head))


if __name__ == "__main__":
    unittest.main()
