# Cracking the code interview - 2.5

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __len__(self):
        if self.next is None:
            return 1
        return 1 + len(self.next)


def sum_inverted(n, p):
    carry = 0

    head = None
    previous = None

    while n or p:
        cur_sum = carry
        carry = 0

        if n:
            cur_sum += n.value
        if p:
            cur_sum += p.value

        if cur_sum >= 10:
           carry = 1 
           cur_sum -= 10

        node = Node(cur_sum)
        
        if previous:
            previous.next = node
            previous = previous.next
        else:
            head = node
            previous = node

        n = n.next if n else None
        p = p.next if p else None

    return head


def left_pad(node, increment):
    head = node
    for i in range(increment):
        head = Node(0, head)
    return head


def sum(n, p):
    n_len = len(n)
    p_len = len(p)

    if n_len > p_len:
        p = left_pad(p, n_len - p_len)
    if p_len > n_len:
        n = left_pad(n, p_len - n_len)

    return sum_impl(n, p)


def sum_impl(n, p):
    if not n and not p:
        return (None, 0)

    cur = sum_impl(n.next if n else None, p.next if p else None)
    cur_sum = n.value + p.value + cur[1]

    carry = 0
    if cur_sum >= 10:
       cur_sum -= 10
       carry = 1

    node = Node(cur_sum)
    node.next = cur[0]

    return (node, carry)


###############################################################
import unittest

def from_list(list):
    idx = 0
    while idx < len(list) - 1:
        list[idx].next = list[idx +1]
        idx += 1 
    return list[0]


def print_ll(head):
    buffer = ""
    node = head
    while node:
        buffer += str(node.value)
        buffer += " -> "
        node = node.next
    print(buffer)


class TestFunctions(unittest.TestCase):
    def test_1(self):
        print("===================")
        n = [Node(1), Node(2), Node(3)]
        p = [Node(1), Node(9), Node(3)]
        
        # 321 + 391 = 712
        print_ll(sum_inverted(from_list(n), from_list(p)))
        # 123 + 193 = 316
        print_ll(sum(from_list(n), from_list(p))[0])

    def test_2(self):
        print("===================")
        # 321 + 94 = 415
        n = [Node(1), Node(2), Node(3)]
        p = [Node(4), Node(9)]
        
        # 123 + 49 = 172
        print_ll(sum_inverted(from_list(n), from_list(p)))
        print_ll(sum(from_list(n), from_list(p))[0])


if __name__ == '__main__':
    unittest.main()









