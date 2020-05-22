def find_range(arr, key):
    def binary_search(arr, key, is_last):
        start, end = 0, len(arr) - 1

        key_index = -1
        while start <= end:
            mid = start + (end - start) // 2

            if key < arr[mid]:
                end = mid - 1
            elif key > arr[mid]:
                start = mid + 1
            else:
                key_index = mid
                if is_last:
                    start = mid + 1
                else:
                    end = mid - 1

        return key_index

    return [binary_search(arr, key, False), binary_search(arr, key, True)]


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
