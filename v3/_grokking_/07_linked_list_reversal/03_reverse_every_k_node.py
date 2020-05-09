from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_every_k_elements(head, k):
    sentinel_head = Node(0)
    sentinel_head.next = head

    previous, current, i = sentinel_head, head, 0
    before, begin, end = None, None, None
    while current:
        i += 1

        if not begin:
            begin = current
            before = previous
        elif i % k == 0:
            end = current
            after = current.next

            current.next = None

            mid_head, mid_tail = reverse(begin)
            before.next = mid_head
            mid_tail.next = after
            begin = None
            current = mid_tail

        previous = current
        current = current.next

    head = sentinel_head.next
    sentinel_head.next = None
    return head


def reverse(head):
    previous, current = None, head
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous, head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end="")
    result.print_list()


main()
