class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        def reverse(node, c):
            stack = []
            while node and c > 0:
                stack.append(node)
                node = node.next
                c -= 1

            tail = stack[-1].next

            for i in range(len(stack) - 1, 0, -1):
                stack[i].next = stack[i - 1]

            stack[0].next = tail
            return stack[-1]

        prev = None
        i = 1
        node = head
        while i < m:
            if not prev:
                head = prev = node
            else:
                prev = node

            node = node.next
            i += 1

        r_head = reverse(node, n - m + 1)

        if not prev:
            return r_head
        else:
            prev.next = r_head
            return head


# ###############################################################
import unittest


def print_ll(head):
    buffer = ""
    node = head
    while node:
        buffer += str(node.val)
        buffer += " -> "
        node = node.next
    print(buffer)


def from_list(lv):
    idx = 0
    l = [ListNode(v) for v in lv]
    while idx < len(l) - 1:
        l[idx].next = l[idx + 1]
        idx += 1
    return l[0]


def equals(l1, l2):
    if l1 is None and l2 is None:
        return True

    if l1 is None or l2 is None:
        return False

    if l1.val != l2.val:
        return False

    return equals(l1.next, l2.next)


class TestFunctions(unittest.TestCase):
    def test_positive(self):
        s = Solution()

        self.assertTrue(
            equals(
                from_list([1, 4, 3, 2, 5]),
                s.reverseBetween(from_list([1, 2, 3, 4, 5]), 2, 4),
            )
        )

        self.assertTrue(
            equals(
                from_list([5, 4, 3, 2, 1]),
                s.reverseBetween(from_list([1, 2, 3, 4, 5]), 1, 5),
            )
        )

        self.assertTrue(
            equals(
                from_list([1, 2, 3, 4, 5]),
                s.reverseBetween(from_list([1, 2, 3, 4, 5]), 1, 1),
            )
        )

        self.assertTrue(
            equals(
                from_list([2, 1, 3, 4, 5]),
                s.reverseBetween(from_list([1, 2, 3, 4, 5]), 1, 2),
            )
        )

        self.assertTrue(
            equals(
                from_list([1, 2, 3, 5, 4]),
                s.reverseBetween(from_list([1, 2, 3, 4, 5]), 4, 5),
            )
        )


if __name__ == "__main__":
    unittest.main()
