def search_ceiling_of_a_number(arr, key):
    start, end = 0, len(arr) - 1

    if key > arr[end]:  # if the 'key' is bigger than the biggest element
        return -1

    while start <= end:
        mid = start + (end - start) // 2

        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:  # found mid = start + (end - start) // 2the key
            return mid

    return start


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
