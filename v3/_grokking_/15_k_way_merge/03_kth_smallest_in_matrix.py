from heapq import *


def find_Kth_smallest(matrix, k):
    number = -1
    heap = []

    for l in matrix: # min(k, len(matrix))
        heappush(heap, (l[0], 0, l))

    for _ in range(k):
        number, idx, lst = heappop(heap)
        if idx < len(lst):
            heappush(heap, (lst[idx + 1], idx + 1, lst))

    return number


def main():
    print(
        "Kth smallest number is: "
        + str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5))
    )


main()
