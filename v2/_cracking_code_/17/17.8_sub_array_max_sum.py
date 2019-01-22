def max_sub_sum(array):
    max_s = max_e = max_sum = cur_s = cur_sum = 0

    for end in range(len(array)):
        cur_sum += array[end]
        
        # Only if the sum is less than 0, the current subarray cannot be part of the 
        # largest sum subarray.
        if cur_sum < 0:
            cur_s = end + 1
            cur_sum = 0
        else:
            if cur_sum > max_sum:
                max_s = cur_s
                max_e = end
                max_sum = cur_sum

    return (max_sum, max_s, max_e)


###############################################################################
import unittest

class Tests(unittest.TestCase):
    def test_bvt(self):
        self.assertEquals((3, 0, 2), max_sub_sum([1, -1, 3, -3, 2]))
        
if __name__ == "__main__":
    unittest.main()
