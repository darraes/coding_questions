def closest(index, target, array):
    return index

def closest_binary_search(target, array, i_range, e_range):
    if i_range == e_range:
        return i_range

    mid = int((i_range + e_range)/2)
    if array[mid] == target: return mid

    if (target < array[mid]): 
        candidate_left = closest_binary_search(target, array, i_range, mid - 1)
        return closest(candidate_left, target, array)
    else: 
        candidate_right = closest_binary_search(target, array, mid + 1, e_range)
        return closest(candidate_right, target, array)

print closest_binary_search(61, [10,20,30,40,50,60,70,80,90], 0, 8)