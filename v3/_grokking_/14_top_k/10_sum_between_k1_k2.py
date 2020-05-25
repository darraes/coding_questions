from heapq import *


def find_sum_of_elements(nums, k1, k2):
    heap = []
    for n in nums:
        heappush(heap, n)

    for _ in range(k1):
        heappop(heap)

    result = 0
    for _ in range(k2 - k1 - 1):
        result += heappop(heap)
    return result


def main():

    print(
        "Sum of all numbers between k1 and k2 smallest numbers: "
        + str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6))
    )
    print(
        "Sum of all numbers between k1 and k2 smallest numbers: "
        + str(find_sum_of_elements([3, 5, 8, 7], 1, 4))
    )


main()
