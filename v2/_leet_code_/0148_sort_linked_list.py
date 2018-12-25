# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        middle = self.find_middle(head)
        right = middle.next
        middle.next = None

        return self.merge(self.sortList(head), self.sortList(right))

    def find_middle(self, node):
        slow = fast = node
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, head1, head2):
        new_head = node = ListNode(-1)

        while head1 and head2:
            if head1.val < head2.val:
                node.next = head1
                head1 = head1.next
            else:
                node.next = head2
                head2 = head2.next
            node = node.next

        node.next = head1 or head2
        return new_head.next


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
        source = [ListNode(7), ListNode(1), ListNode(3), ListNode(5), ListNode(2)]
        head = s.sortList(from_list(source))
        print_ll(head)

        source = [
            ListNode(7),
            ListNode(1),
            ListNode(3),
            ListNode(5),
            ListNode(2),
            ListNode(3),
        ]
        head = s.sortList(from_list(source))
        print_ll(head)

        source = [ListNode(7)]
        head = s.sortList(from_list(source))
        print_ll(head)

        source = [ListNode(7), ListNode(1)]
        head = s.sortList(from_list(source))
        print_ll(head)


if __name__ == "__main__":
    unittest.main()
