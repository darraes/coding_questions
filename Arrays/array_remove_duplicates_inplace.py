# Remove duplicates in place for a sorted array

def clean_array(array):
    if array is not None and len(array) <= 0:
        raise ValueError()

    c = p = 1
    last = array[0]
    while p < len(array):
        if array[p] != last:
            array[c] = array[p]
            c += 1
            last = array[p]
        
        p += 1
        
    return c