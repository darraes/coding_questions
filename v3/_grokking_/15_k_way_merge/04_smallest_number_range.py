from heapq import *


def find_smallest_range(lists):
    max_number, min_range_diff, min_range = 0, 1000000000, [-1, -1]
    heap = []

    for lst in lists:
        max_number = max(max_number, lst[0])
        heappush(heap, (lst[0], 0, lst))

    while True:
        n_min, i, lst = heappop(heap)

        if max_number - n_min < min_range_diff:
            min_range_diff = max_number - n_min
            min_range = [n_min, max_number]

        if i == len(lst) - 1:
            break
        else:
            max_number = max(max_number, lst[i + 1])
            heappush(heap, (lst[i + 1], i + 1, lst))

    return min_range


def main():
    print(
        "Smallest range is: "
        + str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]]))
    )


main()
