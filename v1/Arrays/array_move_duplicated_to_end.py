# Given a sorted array, move the duplicates to the end of the array

######### O(N) SOLUTION ###########
def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def duplicates_to_end(array):
    if array and len(array) <= 0:
        return

    c = p = 1
    last = array[0]
    while p < len(array):
        if array[p] != last:
            last = array[p]
            swap(array, c, p)
            c += 1
            
        p += 1

#### O(N^2) SOLUTION ######
def reverse(array, start, end):
    for i in range((end - start + 1)/2):
        tmp = array[start + i]
        array[start + i] = array[end - i]
        array[end - i] = tmp

def rotate(array, size, start, end):
    reverse(array, start, start + size - 1)
    reverse(array, start + size, end)
    reverse(array, start, end)

def move_duplicates_to_end(array):
    if not array or len(array) <= 1: return

    end, last, i = len(array) - 1, array[0], 1

    while i < range(1, len(array)) and i < end:
        if array[i] == last:

            #decreasing the # of rotation by grouping repetitive elements tail
            #into single rotation
            rotation_size, local_i = 0, i
            while local_i <= end and array[local_i] == last:
                rotation_size += 1
                local_i += 1

            #if we get to local end, then we are handling the last element.
            #The rotation will produce the same result as the original
            if local_i == end: break

            rotate(array, rotation_size, i, end)
            end -= rotation_size
        else:
            last = array[i]
            i += 1


###############################################################
import unittest

class TestFunctions(unittest.TestCase):

    def test_liner(self):
        array = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]
        duplicates_to_end(array)
        self.assertEqual([1, 2, 3, 4, 5, 3, 2, 3, 5, 5, 5], array)

        array = [1, 2, 2, 3, 3, 3, 4, 5]
        duplicates_to_end(array)
        self.assertEqual([1, 2, 3, 4, 5, 3, 2, 3], array)

        array = [1, 1, 1, 2, 2, 3, 3, 3, 4, 5]
        duplicates_to_end(array)
        self.assertEqual([1, 2, 3, 4, 5, 1, 3, 3, 1, 2], array)
    
    ### QUADRATIC
    def test_rotation(self):
        array = [1, 2, 3, 4, 5]

        rotate(array, 2, 0, 4)
        self.assertEqual([3, 4, 5, 1, 2], array)

    def test_move(self):
        array = [1, 2, 2, 3, 3, 3, 4, 5]

        move_duplicates_to_end(array)
        self.assertEqual([1, 2, 3, 4, 5, 3, 3, 2], array)

    def test_tail(self):
        array = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]

        move_duplicates_to_end(array)
        self.assertEqual([1, 2, 3, 4, 5, 5, 5, 5, 3, 3, 2], array)

    def test_head(self):
        array = [1, 1, 1, 2, 2, 3, 3, 3, 4, 5]

        move_duplicates_to_end(array)
        self.assertEqual([1, 2, 3, 4, 5, 3, 3, 2, 1, 1], array)

if __name__ == '__main__':
    unittest.main()