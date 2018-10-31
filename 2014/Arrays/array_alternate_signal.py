# http://www.careercup.com/question?id=5714091033231360

# You are given an array of both negative and positive integers. 
# You need to rearrange the array such that positive and negative numbers alternate. 
# Also, the order should be same as previous array and only O(1) auxiliary space 
# can be used and time complexity boundation O(n). 
# eg. -2 3 4 5 -1 -6 7 9 1 
# result 3 -2 4 -1 5 -6 7 9 1.

##################################################
##################### Solution O(n^2)

# Does the actual alternation of the integers
def alternate(array):
    csm = p = n = 0

    # This method works by having a consumer pointer (csm) receiving either the next 
    # positive number or the next negative 
    while csm < len(array) - 1:
        if array[csm] > 0 and array[csm + 1] < 0:
            pass
        elif array[csm] < 0:
            # Finds the biggest index between the next positive producer and the position
            # right after the consumer
            # This is necessary because the oposite signal "if" can move the consumer
            # ahead and let the other signal producer behind
            p = max(p, csm + 1)
            
            # Searches the next positive number index
            while p < len(array) and array[p] < 0: 
                p += 1
            if p >= len(array): break

            # Swaps the positive number with the consumer location number
            swap(array, p, csm)
            # Moves the number sent to the producer position to the number immediately
            # after the consumer position 
            last_to_front(array, csm + 1, p)
        else:
            # The same logic as for the positive number but for the negative number
            n = max(n, csm + 2)
            while n < len(array) and array[n] > 0: 
                n += 1
            if n >= len(array): break

            swap(array, n, csm + 1)
            last_to_front(array, csm + 2, n)
            
        # Both ifs make that immediate pair (positive, negative) properly positioned
        # due to the last_to_front rotation which makes sure that the number after the 
        # consumer position has the oposite signal    
        csm += 2

    return array
    

# Gets the element on position 'l' and moves to position 'f'
# By doing this, the whole array is shifted making this function O(n)
def last_to_front(array, f, l):
    last = array[l]
    for i in range(f, l):
        array[i + 1] = array[i]
    array[f] = last

# Swaps a single element from the source - s to the destination - d
def swap(array, s, d):
    swap = array[s]
    array[s] = array[d]
    array[d] = swap


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual([3, -2, 4, -1, 5, -6, 7, 9, 1], \
                         alternate([-2, 3, 4, 5, -1, -6, 7, 9, 1]))
        self.assertEqual([4, -2, 5, -3, 7, -1, 9, -6, 1], \
                         alternate([-2, -3, 4, 5, -1, -6, 7, 9, 1]))


if __name__ == '__main__':
    unittest.main()