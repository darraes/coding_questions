from heapq import *


def find_maximum_distinct_elements(nums, k):
    freq, heap = {}, []

    for n in nums:
        if n not in freq:
            freq[n] = 0
        freq[n] += 1

    max_distinct = 0
    for n, f in freq.items():
        if f == 1:
            max_distinct += 1
        else:
            heappush(heap, f)

    while heap and k:
        f = heappop(heap)
        k -= f - 1
        if k >= 0:
            max_distinct += 1

    if k > 0:
        max_distinct -= k

    return max_distinct


def main():

    print(
        "Maximum distinct numbers after removing K numbers: "
        + str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2))
    )
    print(
        "Maximum distinct numbers after removing K numbers: "
        + str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3))
    )
    print(
        "Maximum distinct numbers after removing K numbers: "
        + str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2))
    )


main()
