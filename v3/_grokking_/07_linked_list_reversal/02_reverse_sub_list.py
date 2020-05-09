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


def reverse_sub_list(head, p, q):
    if p == q:
        return head

    previous, last_before, first_after = None, None, None
    n_p, n_q = None, None
    current = head
    while current and current.next:
        if current.value == p:
            last_before = previous
            n_p = current
        elif current.value == q:
            first_after = current.next
            n_q = current
        previous = current   
        current = current.next

    if last_before:
        last_before.next = None
    n_q.next = None

    mid_head, mid_tail = reverse(n_p)
    mid_tail.next = first_after
    if last_before:
        last_before.next = mid_head

    return head if n_p != head else mid_head


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

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end="")
    result.print_list()


    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = reverse_sub_list(head, 1, 3)
    print("Nodes of reversed LinkedList are: ", end="")
    result.print_list()


main()
