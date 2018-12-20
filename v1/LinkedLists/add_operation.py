# Craking the code interview - Linked Lists

class Node:
    def __init__(self, next, value):
        self._next = next
        self._value = value


def add(left, right, carry):
    sum = carry

    if left is not None:
        sum += left._value
    if right is not None:
        sum += right._value
   
    carry = 1 if sum >= 10 else 0
    sum = sum % 10

    if left is not None or right is not None or carry > 0:
        head = Node(None, sum)
        head._next = add(left._next if left is not None else None,\
                         right._next if right is not None else None,\
                         carry)
        return head
    else:
        return None

def print_list(node):
    str = ""
    while node is not None:
        str += "{} -> ".format(node._value)
        node = node._next
    print str






left = Node(Node(Node(Node(Node(None, 5), 5), 5), 3), 1)
right = Node(Node(Node(Node(Node(None, 9), 8), 6), 4), 2)
print_list(left)
print_list(right)
print_list(add(left, right, 0))
print ""
print "---------------------------"
print ""
left = Node(Node(Node(Node(Node(None, 5), 5), 5), 3), 1)
right = None
print_list(left)
print_list(right)
print_list(add(left, right, 0))

print ""
print "---------------------------"
print ""
left = Node(Node(Node(Node(Node(None, 5), 5), 5), 3), 1)
right = Node(None, 9)
print_list(left)
print_list(right)
print_list(add(left, right, 0))

   