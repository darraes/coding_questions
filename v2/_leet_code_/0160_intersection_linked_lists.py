# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        size_a = self.size(headA)
        size_b = self.size(headB)

        if size_a > size_b:
            for _ in range(size_a - size_b):
                headA = headA.next
        elif size_b > size_a:
            for _ in range(size_b - size_a):
                headB = headB.next

        while headB and headA:
            if headB == headA:
                return headA

            headA = headA.next
            headB = headB.next

        return None

    def size(self, node):
        count = 0
        while node:
            count += 1
            node = node.next
        return count


###############################################################
import unittest


def print_ll(head):
    buffer = ""
    node = head
    while node:
        buffer += str(node.val)
        buffer += " -> "
        node = node.next
    print(buffer)


def from_list(list):
    idx = 0
    while idx < len(list) - 1:
        list[idx].next = list[idx + 1]
        idx += 1
    return list[0]


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        source1 = [ListNode(7), ListNode(1), ListNode(3), ListNode(5), ListNode(2)]
        head1 = from_list(source1)
        source2 = [ListNode(70)] + source1[2:]
        head2 = from_list(source2)
        self.assertEqual(source1[2], s.getIntersectionNode(head1, head2))

        source1 = [ListNode(7), ListNode(1), ListNode(3), ListNode(5), ListNode(2)]
        head1 = from_list(source1)
        source2 = [ListNode(70)] + source1
        head2 = from_list(source2)
        self.assertEqual(source1[0], s.getIntersectionNode(head1, head2))

        source1 = [ListNode(7), ListNode(1), ListNode(3), ListNode(5), ListNode(2)]
        head1 = from_list(source1)
        source2 = [ListNode(70)] + source1[4:]
        head2 = from_list(source2)
        self.assertEqual(source1[4], s.getIntersectionNode(head1, head2))

        source1 = [ListNode(7), ListNode(1), ListNode(3), ListNode(5), ListNode(2)]
        head1 = from_list(source1)
        source2 = [ListNode(70)]
        head2 = from_list(source2)
        self.assertEqual(None, s.getIntersectionNode(head1, head2))


if __name__ == "__main__":
    unittest.main()
