# Remove duplicates - Cracking the code interview 1.1

class Node:
    def __init__(self, next, value):
        self.next = next
        self.value = value


def remove_duplicates(head):
    ''' With temporaty buffer '''
    if not head:
        return head

    seen = set()
    seen.add(head.value)

    cur = head
    while cur.next:
        if cur.next.value not in seen:
            seen.add(cur.next.value)
            cur = cur.next
        else:
            cur.next = cur.next.next

    return head


def remove_duplicates_v2(head):
    ''' Without temporaty buffer '''
    if not head:
        return head

    def _remove_if_eq(node):
        if not node:
            return

        target = node.value
        while node.next:
            if node.next.value == target:
                node.next = node.next.next
            else:
                node = node.next

    cur = head
    while cur:
        _remove_if_eq(cur)
        cur = cur.next

    return head



def print_ll(head):
    buffer = ""
    if not head:
        return buffer

    buffer += str(head.value)

    cur = head.next
    while cur:
        buffer += " -> "
        buffer += str(cur.value)
        cur = cur.next

    print buffer


print_ll(remove_duplicates(None))
print_ll(remove_duplicates(Node(None, 4)))
print_ll(remove_duplicates(Node(Node(Node(Node(None, 4), 6), 6), 4)))
print_ll(remove_duplicates(Node(Node(Node(Node(Node(None, 2), 4), 6), 4), 2)))
print_ll(remove_duplicates(Node(Node(Node(Node(None, 4), 6), 6), 4)))
print_ll(remove_duplicates(Node(Node(Node(Node(Node(None, 2), 4), 6), 3), 2)))
print_ll(remove_duplicates(Node(Node(Node(Node(Node(None, 2), 2), 6), 2), 2)))
print_ll(remove_duplicates(Node(Node(Node(Node(Node(None, 2), 2), 2), 2), 2)))


print_ll(remove_duplicates_v2(None))
print_ll(remove_duplicates_v2(Node(None, 4)))
print_ll(remove_duplicates_v2(Node(Node(Node(Node(None, 4), 6), 6), 4)))
print_ll(remove_duplicates_v2(Node(Node(Node(Node(Node(None, 2), 4), 6), 4), 2)))
print_ll(remove_duplicates_v2(Node(Node(Node(Node(None, 4), 6), 6), 4)))
print_ll(remove_duplicates_v2(Node(Node(Node(Node(Node(None, 2), 4), 6), 3), 2)))
print_ll(remove_duplicates_v2(Node(Node(Node(Node(Node(None, 2), 2), 6), 2), 2)))
print_ll(remove_duplicates_v2(Node(Node(Node(Node(Node(None, 2), 2), 2), 2), 2)))




