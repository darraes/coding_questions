class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        if node and node.next:
            swapper = [node.next, node]
            tail = node.next.next

            swapper[0].next = swapper[1]
            swapper[1].next = self.swapPairs(tail)

            return swapper[0]

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

        l1 = from_list([ListNode(1), ListNode(2), ListNode(3), ListNode(4)])
        self.assertTrue(
            equals_ll(
                from_list([ListNode(2), ListNode(1), ListNode(4), ListNode(3)]),
                s.swapPairs(l1),
            )
        )

        l1 = from_list([ListNode(1), ListNode(2), ListNode(3)])
        self.assertTrue(
            equals_ll(
                from_list([ListNode(2), ListNode(1), ListNode(3)]),
                s.swapPairs(l1),
            )
        )

        l1 = from_list([ListNode(1), ListNode(2)])
        self.assertTrue(
            equals_ll(
                from_list([ListNode(2), ListNode(1)]),
                s.swapPairs(l1),
            )
        )


if __name__ == "__main__":
    unittest.main()
