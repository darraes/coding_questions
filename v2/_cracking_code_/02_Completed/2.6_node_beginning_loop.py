def detect_cycle(self, head):
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