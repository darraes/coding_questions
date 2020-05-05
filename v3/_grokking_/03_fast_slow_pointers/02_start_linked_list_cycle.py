from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end="")
            temp = temp.next
        print()


def find_cycle_start(head):
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            break

    k = find_cycle_length(slow)
    return find_start(head, k)


def find_start(head, k):
    p1 = p2 = head

    while k > 0:
        p1 = p1.next
        k -= 1

    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p2


def find_cycle_length(node):
    length = 0
    cur = node

    while True:
        cur = cur.next
        length += 1

        if cur == node:
            break

    return length


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
