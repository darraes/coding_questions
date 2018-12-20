# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        size = self.size(head)
        target = size - n

        if target == 0:
            res = head.next
            head.next = None
            return res

        previous = None
        node = head
        while target > 0:
            previous = node
            node = node.next
            target -= 1

        if previous.next:
            previous.next = previous.next.next

        return head

    def size(self, node):
        count = 0
        while node:
            count += 1
            node = node.next
        return count


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


class TestFunctions(unittest.TestCase):
    def test_1(self):
        print("====================")
        s = Solution()
        head = from_list(
            [
                ListNode(1),
                ListNode(2),
                ListNode(3),
                ListNode(4),
                ListNode(5),
                ListNode(6),
            ]
        )
        print_ll(head)
        print_ll(s.removeNthFromEnd(head, 3))

    def test_2(self):
        print("====================")
        s = Solution()
        head = from_list(
            [
                ListNode(1),
                ListNode(2),
                ListNode(3),
                ListNode(4),
                ListNode(5),
                ListNode(6),
            ]
        )
        print_ll(head)
        print_ll(s.removeNthFromEnd(head, 2))

    def test_3(self):
        print("====================")
        s = Solution()
        head = from_list(
            [
                ListNode(1),
                ListNode(2),
                ListNode(3),
                ListNode(4),
                ListNode(5),
                ListNode(6),
            ]
        )
        print_ll(head)
        print_ll(s.removeNthFromEnd(head, 1))

    def test_4(self):
        print("====================")
        s = Solution()
        head = from_list(
            [
                ListNode(1),
                ListNode(2),
                ListNode(3),
                ListNode(4),
                ListNode(5),
                ListNode(6),
            ]
        )
        print_ll(head)
        print_ll(s.removeNthFromEnd(head, 6))

    def test_5(self):
        print("====================")
        s = Solution()
        head = from_list(
            [
                ListNode(1),
            ]
        )
        print_ll(head)
        print_ll(s.removeNthFromEnd(head, 1))


if __name__ == "__main__":
    unittest.main()
