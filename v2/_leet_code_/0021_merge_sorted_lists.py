# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = current = None

        while l1 or l2:
            if not l1:
                _next = l2
                l2 = l2.next
            elif not l2:
                _next = l1
                l1 = l1.next
            else:
                if l1.val < l2.val:
                    _next = l1
                    l1 = l1.next
                else:
                    _next = l2
                    l2 = l2.next
            if not current:
                head = current = _next
            else:
                current.next = _next
                current = current.next

        return head


###############################################################
import unittest


def from_list(list):
    idx = 0
    while idx < len(list) - 1:
        list[idx].next = list[idx + 1]
        idx += 1
    return list[0]


def print_ll(head):
    buffer = ""
    node = head
    while node:
        buffer += str(node.val)
        buffer += " -> "
        node = node.next
    print(buffer)


def equals_ll(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next

    return l1 is None and l2 is None


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        l1 = from_list([ListNode(1), ListNode(2), ListNode(4)])
        l2 = from_list([ListNode(1), ListNode(3), ListNode(4)])

        self.assertTrue(
            equals_ll(
                from_list(
                    [
                        ListNode(1),
                        ListNode(1),
                        ListNode(2),
                        ListNode(3),
                        ListNode(4),
                        ListNode(4),
                    ]
                ),
                s.mergeTwoLists(l1, l2),
            )
        )


    def test_2(self):
        s = Solution()
        l1 = from_list([ListNode(1), ListNode(2), ListNode(4)])
        l2 = from_list([ListNode(1), ListNode(3), ListNode(4)])

        self.assertFalse(
            equals_ll(
                from_list(
                    [
                        ListNode(1),
                        ListNode(1),
                        ListNode(2),
                        ListNode(3),
                        ListNode(4),
                    ]
                ),
                s.mergeTwoLists(l1, l2),
            )
        )


    def test_3(self):
        s = Solution()
        l1 = from_list([ListNode(1)])
        l2 = from_list([ListNode(1), ListNode(3), ListNode(4)])

        self.assertTrue(
            equals_ll(
                from_list(
                    [
                        ListNode(1),
                        ListNode(1),
                        ListNode(3),
                        ListNode(4),
                    ]
                ),
                s.mergeTwoLists(l1, l2),
            )
        )


    def test_4(self):
        s = Solution()
        l2 = from_list([ListNode(1), ListNode(3), ListNode(4)])

        self.assertTrue(
            equals_ll(
                from_list(
                    [
                        ListNode(1),
                        ListNode(3),
                        ListNode(4),
                    ]
                ),
                s.mergeTwoLists(None, l2),
            )
        )


if __name__ == "__main__":
    unittest.main()
