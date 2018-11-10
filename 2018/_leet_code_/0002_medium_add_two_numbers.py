# https://leetcode.com/problems/add-two-numbers/description/

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0

        head = None
        previous = None

        while l1 or l2 or carry > 0:
            cur_sum = carry
            carry = 0

            if l1:
                cur_sum += l1.val
            if l2:
                cur_sum += l2.val

            if cur_sum >= 10:
               carry = 1 
               cur_sum -= 10

            node = ListNode(cur_sum)
            
            if previous:
                previous.next = node
                previous = previous.next
            else:
                head = node
                previous = node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head


###############################################################
import unittest

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def from_list(list):
    idx = 0
    while idx < len(list) - 1:
        list[idx].next = list[idx +1]
        idx += 1 
    return list[0]


def equals(l1, l2):
    if l1 is None and l2 is None:
        return True

    if l1 is None or l2 is None:
        return False

    if l1.val != l2.val:
        return False

    return equals(l1.next, l2.next)


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        n = [ListNode(1), ListNode(2), ListNode(3)]
        p = [ListNode(1), ListNode(9), ListNode(3)]
        res = [ListNode(2), ListNode(1), ListNode(7)]
        
        self.assertTrue(equals(from_list(res),
                          s.addTwoNumbers(from_list(n), from_list(p))))

    def test_2(self):
        s = Solution()
        n = [ListNode(1), ListNode(2), ListNode(3)]
        p = [ListNode(4), ListNode(9)]
        res = [ListNode(5), ListNode(1), ListNode(4)]
        
        self.assertTrue(equals(from_list(res),
                          s.addTwoNumbers(from_list(n), from_list(p))))
        self.assertTrue(equals(from_list(res),
                          s.addTwoNumbers(from_list(p), from_list(n))))

    def test_3(self):
        s = Solution()
        n = [ListNode(1), ListNode(2), ListNode(3)]
        p = [ListNode(0)]
        res = [ListNode(1), ListNode(2), ListNode(3)]
        
        self.assertTrue(equals(from_list(res),
                          s.addTwoNumbers(from_list(n), from_list(p))))

    def test_4(self):
        s = Solution()
        n = [ListNode(0)]
        p = [ListNode(0)]
        res = [ListNode(0)]
        
        self.assertTrue(equals(from_list(res),
                          s.addTwoNumbers(from_list(n), from_list(p))))

    def test_5(self):
        s = Solution()
        n = [ListNode(5)]
        p = [ListNode(5)]
        res = [ListNode(0), ListNode(1)]
        
        self.assertTrue(equals(from_list(res),
                          s.addTwoNumbers(from_list(n), from_list(p))))

if __name__ == '__main__':
    unittest.main()