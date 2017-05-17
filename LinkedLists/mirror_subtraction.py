# http://www.careercup.com/question?id=5657550909341696

class Node:
    def __init__(self, next, value):
        self._next = next
        self._value = value

def revert(node):
    if node == None: raise
    elif node._next == None:
        return (node, node)
    else:
        tail, head = revert(node._next)
        tail._next = node
        node._next = None
        return (node, head)

def solve(node):
    slow = fast = firstHalf = node
    secondHalf = None

    while slow._next != None:
        if fast._next == None or fast._next._next == None:
            secondHalf = slow._next
            slow._next = None
            break
        else:
            slow = slow._next
            fast = fast._next._next

    headF = firstHalf
    tailF = slow

    tail, secondHalf = revert(secondHalf)
    headS = secondHalf

    while firstHalf != None:
        if secondHalf != None:
            firstHalf._value -= secondHalf._value
            secondHalf = secondHalf._next
        else:
            firstHalf._value = 0
        firstHalf = firstHalf._next
        
    tail, headS = revert(headS)
    tailF._next = headS

    return headF

head = Node(Node(Node(Node(Node(None, 10), 5), 4), 9), 10)
new = solve(head)