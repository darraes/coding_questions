class Node:
    def __init__(self, value, next=None):
        self.next = next
        self.value = value

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node = runner = head
        while runner and runner.next:
            node = node.next
            runner = runner.next.next
            if node == runner:
                intersect = head
                while node != intersect:
                    node = node.next
                    intersect = intersect.next
                return node

        return None


###############################################################
import unittest


def from_list(list):
    idx = 0
    while idx < len(list) - 1:
        list[idx].next = list[idx + 1]
        idx += 1
    return list[0]


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        source = [Node(1), Node(2), Node(3), Node(5), Node(7)]
        n = from_list(source)
        source[-1].next = source[1]
        s.detectCycle(n)


if __name__ == "__main__":
    unittest.main()
