# http://www.careercup.com/question?id=4909367207919616

# WAP to modify the array such that arr[I] = arr[arr[I]]. 
# Do this in place i.e. with out using additional memory. 

# example : if a = {2,3,1,0} 
# o/p = a = {1,0,3,2} 

# Note : The array contains 0 to n-1 integers.

# It is possible to store 2 numbers within one if you use the remainder for one
# and the integer division for other
def i_swap(array):
    length = len(array)
    for i in range(length):
        new = length * (array[array[i] % length] % length)
        array[i] = array[i] + new

    for i in range(length):
        array[i] /= length

    return array

print (i_swap([2, 3, 1, 0]))