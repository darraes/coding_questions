# http://www.careercup.com/question?id=5652354158297088

# You're given an array of integers(eg [3,4,7,1,2,9,8]) 
# Find the index of values that satisfy A+B = C + D, where A,B,C & D 
# are integers values in the array. 

# Eg: Given [3,4,7,1,2,9,8] array 
# The following 
# 3 + 7 = 1 + 9 satisfies A+B=C+D 
# so print (0,2,3,5)

def equals_sum(array):
    sums = dict()
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            sum = array[i] + array[j]
            # When we hit a sum seen before, we can just return both pair of 
            # indexes
            if sum in sums:
                return (sum, (sums[sum]), (i, j))
            else:
            # Every possible sum gets saved pointing to its indexes.
                sums[sum] = (i, j)
            

print equals_sum([3,4,7,1,2,9,8])