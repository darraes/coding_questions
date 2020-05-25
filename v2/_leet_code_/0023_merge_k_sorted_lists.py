import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []

        for l in lists:
            if l:
                heap.append((l.val, l))

        heapq.heapify(heap)

        head = node = None
        while len(heap) > 0:
            _, next_node = heapq.heappop(heap)
            if not node:
                head = node = next_node
            else:
                node.next = next_node
                node = node.next

            if next_node.next:
                heapq.heappush(heap, (next_node.next.val, next_node.next))

        if node:
            node.next = None
        return head


####### =============== TESTS ===============
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
        s = Solution()
        l = s.mergeKLists(
            [
                from_list([ListNode(2), ListNode(4)]),
                from_list([ListNode(1), ListNode(3)]),
            ]
        )
        print_ll(l)

        s = Solution()
        l = s.mergeKLists(
            [from_list([ListNode(2)]), from_list([ListNode(1), ListNode(3)])]
        )
        print_ll(l)

        s = Solution()
        l = s.mergeKLists(
            [from_list([ListNode(1), ListNode(3)]), from_list([ListNode(2)])]
        )
        print_ll(l)

        s = Solution()
        l = s.mergeKLists([])


if __name__ == "__main__":
    unittest.main()
