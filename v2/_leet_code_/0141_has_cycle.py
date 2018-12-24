# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node = head

        runner = None
        if node:
            runner = node.next

        while node and runner and runner.next:
            if node == runner:
                return True

            node = node.next
            runner = runner.next.next
        return False