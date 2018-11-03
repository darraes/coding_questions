# Given an integer array and a window size, calculate the max different
# between the integer of all windows
# 
# ### ====== requires Python 3
from collections import deque

def update_window(window, to_add, to_remove = None):
    ''' For simplicity we are using a deque as a sorted list that allows us
        to add and remove on O(n) and compute the distance in O(1)
        A structure like a B-Tree or an AVL Tree would allow allow everything to
        be computed on O(log(n))
    '''
    # will remove the first occurence
    if to_remove:
        window.remove(to_remove)

    # Does a sorted insertion
    idx = 0
    while idx < len(window):
        element = window[idx]
        if element > to_add:
            break
        idx += 1

    window.insert(idx, to_add)


def compute_diff(window):
    return window[-1] - window[0]


def compute_max_diff(input, window_size):
    max_distance = None

    rm_idx = 0
    add_idx = window_size - 1
    window = deque()

    if len(input) < window_size:
        raise ValueError()

    for i in range(window_size):
        update_window(window, input[i])

    max_distance = compute_diff(window)

    add_idx += 1
    while add_idx < len(input):
        update_window(window, input[add_idx], input[rm_idx])
        rm_idx += 1
        add_idx += 1

        cur_distance = compute_diff(window)
        max_distance = max_distance if max_distance > cur_distance \
                                    else cur_distance

    return max_distance

        
###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        distance = compute_max_diff([1, 14, 12, 17, 8, 9, 45, 12, 16, 8], 5)
        self.assertEqual(37, distance)

        distance = compute_max_diff([2, 1, 1, 1, 1, 3, 1, 2, 1, 1], 5)
        self.assertEqual(2, distance)


if __name__ == '__main__':
    unittest.main()