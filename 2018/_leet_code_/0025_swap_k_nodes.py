class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from collections import deque


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        node = head
        head = prev = None

        while node:
            i = 0
            level = deque()
            while i < k and node:
                level.appendleft(node)
                node = node.next
                i += 1

            if i < k:
                level.reverse()

            for j in range(len(level) - 1):
                level[j].next = level[j + 1]

            if prev:
                prev.next = level[0]

            prev = level[-1]
            prev.next = None

            if not head:
                head = level[0]

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
    # print_ll(l2)
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next

    return l1 is None and l2 is None


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        l1 = from_list([ListNode(1), ListNode(2), ListNode(3), ListNode(4)])
        self.assertTrue(
            equals_ll(
                from_list([ListNode(2), ListNode(1), ListNode(4), ListNode(3)]),
                s.reverseKGroup(l1, 2),
            )
        )

        l1 = from_list([ListNode(1), ListNode(2), ListNode(3)])
        self.assertTrue(
            equals_ll(
                from_list([ListNode(2), ListNode(1), ListNode(3)]),
                s.reverseKGroup(l1, 2),
            )
        )

        l1 = from_list([ListNode(1), ListNode(2)])
        self.assertTrue(
            equals_ll(from_list([ListNode(2), ListNode(1)]), s.reverseKGroup(l1, 2))
        )

    def test_2(self):
        s = Solution()

        l1 = from_list(
            [ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)]
        )
        self.assertTrue(
            equals_ll(
                from_list(
                    [ListNode(3), ListNode(2), ListNode(1), ListNode(4), ListNode(5)]
                ),
                s.reverseKGroup(l1, 3),
            )
        )

        l1 = from_list([ListNode(1), ListNode(2), ListNode(3), ListNode(4)])
        self.assertTrue(
            equals_ll(
                from_list([ListNode(3), ListNode(2), ListNode(1), ListNode(4)]),
                s.reverseKGroup(l1, 3),
            )
        )

        l1 = from_list([ListNode(1), ListNode(2), ListNode(3)])
        self.assertTrue(
            equals_ll(
                from_list([ListNode(3), ListNode(2), ListNode(1)]),
                s.reverseKGroup(l1, 3),
            )
        )

        l1 = from_list([ListNode(1), ListNode(2)])
        self.assertTrue(
            equals_ll(from_list([ListNode(1), ListNode(2)]), s.reverseKGroup(l1, 3))
        )

        l1 = ListNode(1)
        self.assertTrue(equals_ll(ListNode(1), s.reverseKGroup(l1, 3)))

        l1 = None
        self.assertTrue(equals_ll(None, s.reverseKGroup(l1, 3)))


if __name__ == "__main__":
    unittest.main()
