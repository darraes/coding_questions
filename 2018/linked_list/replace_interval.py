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
    def __init__(self, lower, upper, after = None):
        self.lower = lower
        self.upper = upper
        self.after = after

    def __str__(self):
        return "[{}, {})".format(self.lower, self.upper)

    def __eq__(self, that):
        return self.lower == that.lower and self.upper == that.upper


def connect_lower(interval, lower_node, head, before_lower_intersect):
    if interval.lower > lower_node.lower:
        lower_node.upper = interval.lower
        lower_node.after = interval
    else:
        if not before_lower_intersect:
                head = interval
        else:
            before_lower_intersect.after = interval
    return head


def connect_upper(interval, upper_node, head):
    if head == upper_node:
        head = interval

    if interval.upper < upper_node.upper:
        upper_node.lower = interval.upper
        interval.after = upper_node
    else:
        interval.after = upper_node.after

    return head



def add_interval(head, interval):
    # First step is to find the node where the lower interval intersects
    before_lower_intersect = None
    lower_intersect = None
    node = head
    while node:
        if interval.lower >= node.lower and interval.lower < node.upper:
            lower_intersect = node
            break 
        before_lower_intersect = node
        node = node.after

    # First step is to find the node where the upper interval intersects
    upper_intersect = None
    node = head
    while node:
        if interval.upper > node.lower and interval.upper <= node.upper:
            upper_intersect = node
            break
        node = node.after

    # At this point, the new interval will be intersecting with either one node
    # or multiple nodes. It can also be at the begining or end - no intersection
    
    # If there are no intersections, the new interval is either the new head or
    # the new tail
    if not lower_intersect and not upper_intersect:
        if interval.upper <= head.lower:
            interval.after = head
            head = interval
        else:
            node = head
            while node.after:
                node = node.after
            node.after = interval
        return head
    
    # TODO: Case where the new node is replacing or inside a single node
    if lower_intersect and upper_intersect and \
            lower_intersect == upper_intersect:
        return

    # Case where the new interval has a multiple nodes fan-out
    if lower_intersect:
        head = connect_lower(
            interval, lower_intersect, head, before_lower_intersect)
        
    if upper_intersect:
        head = connect_upper(interval, upper_intersect, head)

    return head


###############################################################
import unittest

def from_list(list):
    idx = 0
    while idx < len(list) - 1:
        list[idx].after = list[idx +1]
        idx += 1 
    return list[0]


def print_intervals(head):
    buffer = ""
    node = head
    while node:
        buffer += str(node)
        buffer += " -> "
        node = node.after
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

if __name__ == '__main__':
    unittest.main()















