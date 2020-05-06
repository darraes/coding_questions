def dutch_flag_sort(arr):
    low, high = 0, len(arr) - 1
    i = 0

    while i < high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            low += 1
            i += 1
        elif arr[i] == 2:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1
        else:
            i += 1

    return

