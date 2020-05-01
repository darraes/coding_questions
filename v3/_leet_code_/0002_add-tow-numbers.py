from list_utils import from_list, equals

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = current = ListNode(0)
        carry = 0

        while l1 or l2 or carry > 0:
            value = carry
            carry = 0

            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next

            carry = value // 10
            value = value % 10

            current.val = value

            if l1 or l2 or carry > 0:
                current.next = ListNode(0)
                current = current.next

        return head


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertTrue(
            equals(
                from_list([ListNode(7), ListNode(0), ListNode(8)]),
                s.addTwoNumbers(
                    from_list([ListNode(2), ListNode(4), ListNode(3)]),
                    from_list([ListNode(5), ListNode(6), ListNode(4)]),
                ),
            )
        )
        self.assertTrue(
            equals(
                from_list([ListNode(7), ListNode(0), ListNode(3), ListNode(1)]),
                s.addTwoNumbers(
                    from_list([ListNode(2), ListNode(4), ListNode(3)]),
                    from_list([ListNode(5), ListNode(6), ListNode(9)]),
                ),
            )
        )
        self.assertTrue(
            equals(
                from_list([ListNode(1), ListNode(1), ListNode(3), ListNode(1)]),
                s.addTwoNumbers(
                    from_list([ListNode(6), ListNode(4), ListNode(3)]),
                    from_list([ListNode(5), ListNode(6), ListNode(9)]),
                ),
            )
        )
        self.assertTrue(
            equals(
                from_list([ListNode(0), ListNode(0), ListNode(2)]),
                s.addTwoNumbers(
                    from_list([ListNode(0), ListNode(0), ListNode(1)]),
                    from_list([ListNode(0), ListNode(0), ListNode(1)]),
                ),
            )
        )


if __name__ == "__main__":
    unittest.main()
