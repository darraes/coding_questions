 # http://www.careercup.com/question?id=4852029923000320

def binary_search(target, array, i_range, e_range):
    if i_range > e_range: return -1
    mid = int((i_range + e_range)/2)
    if array[mid] == target: return mid
    if (target < array[mid]): return binary_search(target, array, i_range, mid - 1)
    else: return binary_search(target, array, mid + 1, e_range)


def rotated_binary_search(target, array, i_range, e_range):
    if i_range > e_range: return -1
    mid = int((i_range + e_range)/2)
    if array[mid] == target: return mid
    if array[i_range] < array[mid]: 
        if target < array[mid] and target >= array[i_range]:
            return binary_search(target, array, i_range, mid - 1)
        else:
            return rotated_binary_search(target, array, mid + 1, e_range)        
    else:
        if target > array[mid] and target <= array[e_range]:
            return binary_search(target, array, mid + 1, e_range)
        else:
            return rotated_binary_search(target, array, i_range, mid - 1)



#print binary_search(7, [1,2,3,4,5,6,7,8,9], 0, 8)
print rotated_binary_search(1, [4,5,6,7,8,9,1,2,3], 0, 8)
print rotated_binary_search(2, [4,5,6,7,8,9,1,2,3], 0, 8)
print rotated_binary_search(3, [4,5,6,7,8,9,1,2,3], 0, 8)
print rotated_binary_search(4, [4,5,6,7,8,9,1,2,3], 0, 8)
print rotated_binary_search(5, [4,5,6,7,8,9,1,2,3], 0, 8)
print rotated_binary_search(6, [4,5,6,7,8,9,1,2,3], 0, 8)
print rotated_binary_search(7, [4,5,6,7,8,9,1,2,3], 0, 8)
print rotated_binary_search(8, [4,5,6,7,8,9,1,2,3], 0, 8)
