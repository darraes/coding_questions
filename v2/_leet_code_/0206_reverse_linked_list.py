# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        while head:
            stack.append(head)
            head = head.next
            stack[-1].next = None

        head = node = None
        while len(stack) > 0:
            if not node:
                head = node = stack.pop()
            else:
                node.next = stack.pop()
                node = node.next

        return head

    def reverseListRec(self, node):
        if node is None:
            return (None, None)
        if node.next is None:
            return (node, node)

        head, tail = self.reverseListRec(node.next)
        node.next = None
        tail.next = node

        return head, node


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
        print_ll(s.reverseList(head))

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
        print_ll(s.reverseListRec(head)[0])

    def test_3(self):
        print("====================")
        s = Solution()
        head = from_list([ListNode(1)])
        print_ll(head)
        print_ll(s.reverseListRec(head)[0])

    def test_4(self):
        print("====================")
        s = Solution()
        head = from_list([ListNode(1), ListNode(2)])
        print_ll(head)
        print_ll(s.reverseListRec(head)[0])


if __name__ == "__main__":
    unittest.main()
