# Cracking the code interview - Linked Lists

class Node:
    def __init__(self, next, value):
        self._next = next
        self._value = value


def _add(left, right):
    if left is None: return None, 0

    head, carry = _add(left._next, right._next)

    sum = left._value + right._value + carry
    carry = 1 if sum > 9 else 0
    sum = sum % 10

    node = Node(head, sum)

    return node, carry


def add(left, right):
    l_size = size(left)
    r_size = size(right)

    if l_size > r_size:
        right = zero_fill(right, l_size - r_size)
    elif r_size > l_size:
        left = zero_fill(left, r_size - l_size)

    head, carry = _add(left, right)

    if carry == 1:
        return Node(head, 1)
    else:
        return head


def zero_fill(node, count):
    for i in range(count):
        node = Node(node, 0)
    return node


def size(node):
    size = 0;
    while node is not None:
        size += 1
        node = node._next
    return size


def print_list(node):
    str = ""
    while node is not None:
        str += "{} -> ".format(node._value)
        node = node._next
    print str


left = Node(Node(Node(Node(None, 5), 5), 3), 1)
right = Node(Node(Node(Node(Node(None, 9), 8), 6), 4), 2)
print_list(left)
print_list(right)
print_list(add(left, right))
print ""
print "---------------------------"
print ""