# Craking the code interview - Linked Lists

class Node:
    def __init__(self, next, value):
        self._next = next
        self._value = value

def merge(left, right):
    head = None
    index = Node(None, -1) #dummy node

    while (left is not None or right is not None):
        if (left is not None and right is not None):
            if left._value < right._value:
                index._next = left;
                left = left._next
            else:
                index._next = right;
                right = right._next
        elif left is not None:
            index._next = left;
            left = left._next
        else:
            index._next = right;
            right = right._next
        index = index._next        
        if head is None:
            head = index

    return head

left = Node(Node(Node(Node(Node(None, 90), 70), 50), 3), 1)
right = Node(Node(Node(Node(Node(None, 10), 8), 6), 4), 2)

together = merge(left, right)
