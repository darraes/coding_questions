# http://www.careercup.com/question?id=6261752413028352

#Two finite, strictly increasing, integer sequences are given. Any common integer between 
#the two sequences constitute an intersection point. Take for example the following 
#two sequences where intersection points are printed in bold: 

#First= 3 5 7 9 20 25 30 40 55 56 57 60 62 
#Second= 1 4 7 11 14 25 44 47 55 57 100 

#You can walk over these two sequences in the following way: 
#1. You may start at the beginning of any of the two sequences. Now start moving forward. 
#2. At each intersection point, you have the choice of either continuing with the same sequence 
#you're currently on, or switching to the other sequence. 
#The objective is finding a path that produces the maximum sum of data you walked over. In the 
#above example, the largest possible sum is 450 which is the result of 
#adding 3, 5, 7, 9, 20, 25, 44, 47, 55, 56, 57, 60, and 62


def calculate(array1, array2):
	jumps1 = dict()
	jumps2 = dict()

	# Creates the jumps which are dict from the intersections (values) to
    # indexes
	for i in range(len(array1)):
		jumps1[array1[i]] = i
	for i in range(len(array2)):
		jumps2[array2[i]] = i

	# Get the max starting from both sequences
	return max(calculate_internal(
                   0, (1, array1), (2, array2), jumps1, jumps2, dict()), 
			       calculate_internal(
                   0, (2, array2), (1, array1), jumps2, jumps1, dict()))
			   

def calculate_internal(i, c_array, o_array, c_jumps, o_jumps, cache):
	# The parameters starting with c_ represent the current sequence and jumps
	# The ones starting with o_ represent the 'other' sequence and jumps
	
	if i >= len(c_array[1]):    
		return 0
	else:
		# Since this is clearly a DP problem, we use a cache to hold computed
        # sequences
		if (i, c_array[0]) in cache:
			return cache[(i, c_array[0])]
		
		# For every given start and array, we can always compute the cost of
        # just moving forward within the same sequence
		sum = c_array[1][i] + calculate_internal(i + 1,
                                                 c_array,
                                                 o_array,
												 c_jumps,
                                                 o_jumps,
                                                 cache)
		if o_jumps.has_key(c_array[1][i]):
			
			# If there is a jump, we get the index of that jump on the other array 
            # and use it to navigate to the other array
			j = o_jumps[c_array[1][i]]
			sum = max(sum, c_array[1][i] + calculate_internal(j + 1,
                                                              o_array,
													          c_array,
                                                              o_jumps,
                                                              c_jumps,
                                                              cache))

		cache[(i, c_array[0])] = sum
		return sum


###############################################################################
import unittest

class Tests(unittest.TestCase):
    def test_bvt(self):
        self.assertEquals(37, calculate([2, 5, 8, 9], [5, 6, 7, 8]))
        self.assertEquals(450, 
            calculate([3, 5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62], \
                      [1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100]))
        
if __name__ == "__main__":
    unittest.main()
