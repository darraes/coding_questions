from heapq import *

def find_k_frequent_numbers(nums, k):
    topNumbers = []
    frequencies = {}

    for n in nums:
        if n not in frequencies:
            frequencies[n] = 0
        frequencies[n] += 1
             
    for n, f in frequencies.items():
        heappush(topNumbers, (f, n))
        if len(topNumbers) > k:
            heappop(topNumbers)


    return topNumbers


def main():

    print(
        "Here are the K frequent numbers: "
        + str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2))
    )

    print(
        "Here are the K frequent numbers: "
        + str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2))
    )


main()
