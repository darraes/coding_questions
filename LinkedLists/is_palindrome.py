from collections import deque

class Node:
    def __init__(self, next, value):
        self._next = next
        self._value = value

#Recursive Solution
def _is_palindrome(node, runner):
    if node is None or runner is None: return (True, node)
    if runner._next is None: return (True, node._next)

    result, to_compare = _is_palindrome(node._next, runner._next._next)

    if result and node._value == to_compare._value: return (True,  to_compare._next)
    else: return (False, to_compare._next)

def is_palindrome(node):
    return _is_palindrome(node, node)


# Iterative Solution
def is_palindrome_nr(node):
    if node is None: return True

    stack = deque()
    slow = node
    fast = node

    ##We could already add slow to the queue for further comparison
    while fast is not None and fast._next is not None:
        slow = slow._next
        fast = fast._next._next

    if fast is not None:
        slow = slow._next

    while slow is not None:
        stack.append(slow)
        slow = slow._next

    while len(stack) > 0:
        p = stack.pop();

        if node._value != p._value: return False
        node = node._next

    return True



print is_palindrome(Node(Node(Node(Node(Node(None, 2), 4), 6), 4), 2))
print is_palindrome(Node(Node(Node(Node(None, 4), 6), 6), 4))
print is_palindrome(Node(Node(Node(Node(Node(None, 2), 4), 6), 3), 2))
print is_palindrome(Node(None, 2))
print is_palindrome(Node(Node(None, 2), 2))
print is_palindrome(Node(Node(None, 2), 3))

print is_palindrome_nr(Node(Node(Node(Node(Node(None, 2), 4), 6), 4), 2))
print is_palindrome_nr(Node(Node(Node(Node(None, 4), 6), 6), 4))
print is_palindrome_nr(Node(Node(Node(Node(Node(None, 2), 4), 6), 3), 2))
print is_palindrome_nr(Node(None, 2))
print is_palindrome_nr(Node(Node(None, 2), 2))
print is_palindrome_nr(Node(Node(None, 2), 3))

