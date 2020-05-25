from heapq import *


def find_k_largest_numbers(nums, k):
    result = []

    for n in nums:
        heappush(result, n)
        if len(result) > k:
            heappop(result)

    return result


def main():

    print(
        "Here are the top K numbers: "
        + str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3))
    )

    print(
        "Here are the top K numbers: "
        + str(find_k_largest_numbers([5, 12, 11, -1, 12], 3))
    )


main()
