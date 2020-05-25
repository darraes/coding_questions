from heapq import *


def find_Kth_smallest(lists, k):
    number = -1
    kth = 0
    heap = []

    for idx, l in enumerate(lists):
        heappush(heap, (l[0], 0, l))

    while heap:
        kth += 1
        n, i, lst = heappop(heap)
        if kth == k:
            return n

        if i < len(lst) - 1:
            heappush(heap, (lst[i + 1], i + 1, lst))
    return -1


def main():
    print(
        "Kth smallest number is: "
        + str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5))
    )


main()
