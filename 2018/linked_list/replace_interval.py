# Given a list of intervals [x, y) with any gaps and a interval [a, b) design
# an algorithm that will properly introduce the interval in the list without
# creating any gaps or intersections
# Ex
# <list>: [0, 1)[1, 5)[5, 10)
# <intr>: [2, 7)
# result: [0, 1)[1, 2)[2, 7)[7, 10)
# 
# PS: Assume the input is valid and will always produce a proper output


class IntervalNode:
    def __init__(self, lower, upper, next = None):
        self.lower = lower
        self.upper = upper
        self.next = next

    def __str__(self):
        return "[{}, {})".format(self.lower, self.upper)

    def __eq__(self, that):
        return self.lower == that.lower and self.upper == that.upper


def add_interval(head, interval):
    # First step is to find the node where the lower interval intersects
    lower_intersect = None
    node = head
    while node:
        if interval.lower <= node.upper and interval.lower > node.lower:
            lower_intersect = node
            break 
        node = node.next

    # First step is to find the node where the upper interval intersects
    upper_intersect = None
    node = head
    while node:
        if interval.upper >= node.lower and interval.upper < node.upper:
            upper_intersect = node
            break
        node = node.next

    # Corner case where the new interval is inside a single know interval
    if lower_intersect and upper_intersect and \
            lower_intersect == upper_intersect:
        after = IntervalNode(interval.upper, lower_intersect.upper)
        after.next = lower_intersect.next
        interval.next = after

        lower_intersect.upper = interval.lower
        lower_intersect.next = interval

        return head

    # Lower and upper boundaries of the new interval don't intersect with the
    # same known interval
    if lower_intersect:
        lower_intersect.upper = interval.lower
        lower_intersect.next = interval

    if upper_intersect:
        if upper_intersect == head:
            head = interval
        upper_intersect.lower = interval.upper
        interval.next = upper_intersect

    return head


###############################################################
import unittest

def from_list(list):
    idx = 0
    while idx < len(list) - 1:
        list[idx].next = list[idx +1]
        idx += 1 
    return list[0]


def print_intervals(head):
    buffer = ""
    node = head
    while node:
        buffer += str(node)
        buffer += " -> "
        node = node.next
    print(buffer)

class TestFunctions(unittest.TestCase):
    def test_1(self):
        print("===================")
        intervals = [IntervalNode(0, 1),
                     IntervalNode(1, 5),
                     IntervalNode(5, 10),
                     IntervalNode(10, 15)]
        new_interval = IntervalNode(2, 7)
        
        head = from_list(intervals)
        print_intervals(head)
        result = add_interval(head, new_interval)
        print_intervals(result)

    def test_2(self):
        print("===================")
        intervals = [IntervalNode(0, 1),
                     IntervalNode(1, 5),
                     IntervalNode(5, 10),
                     IntervalNode(10, 15)]
        new_interval = IntervalNode(1, 10)
        
        head = from_list(intervals)
        print_intervals(head)
        result = add_interval(head, new_interval)
        print_intervals(result)

    def test_3(self):
        print("===================")
        intervals = [IntervalNode(0, 1),
                     IntervalNode(1, 5),
                     IntervalNode(5, 10),
                     IntervalNode(10, 15)]
        new_interval = IntervalNode(-1, 0)
        
        head = from_list(intervals)
        print_intervals(head)
        result = add_interval(head, new_interval)
        print_intervals(result)

    def test_4(self):
        print("===================")
        intervals = [IntervalNode(0, 1),
                     IntervalNode(1, 5),
                     IntervalNode(5, 10),
                     IntervalNode(10, 15)]
        new_interval = IntervalNode(15, 20)
        
        head = from_list(intervals)
        print_intervals(head)
        result = add_interval(head, new_interval)
        print_intervals(result)

    def test_5(self):
        print("===================")
        intervals = [IntervalNode(1, 3),
                     IntervalNode(3, 5),
                     IntervalNode(5, 10),
                     IntervalNode(10, 15)]
        new_interval = IntervalNode(0, 2)
        
        head = from_list(intervals)
        print_intervals(head)
        result = add_interval(head, new_interval)
        print_intervals(result)

    def test_6(self):
        print("===================")
        intervals = [IntervalNode(1, 3),
                     IntervalNode(3, 5),
                     IntervalNode(5, 10),
                     IntervalNode(10, 15)]
        new_interval = IntervalNode(6, 9)
        
        head = from_list(intervals)
        print_intervals(head)
        result = add_interval(head, new_interval)
        print_intervals(result)

if __name__ == '__main__':
    unittest.main()















