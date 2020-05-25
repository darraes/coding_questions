from heapq import *


def find_closest_elements(arr, K, X):
    result = []

    for n in arr:
        heappush(result, (-abs(n - X), n))
        if len(result) > K:
            heappop(result)

    return [t[1] for t in result]


def main():
    print(
        "'K' closest numbers to 'X' are: "
        + str(find_closest_elements([5, 6, 7, 8, 9], 3, 7))
    )
    print(
        "'K' closest numbers to 'X' are: "
        + str(find_closest_elements([2, 4, 5, 6, 9], 3, 6))
    )
    print(
        "'K' closest numbers to 'X' are: "
        + str(find_closest_elements([2, 4, 5, 6, 9], 3, 10))
    )


main()
