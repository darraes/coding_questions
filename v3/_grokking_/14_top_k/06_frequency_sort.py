from heapq import *

def sort_character_by_frequency(str):
    freq, heap = {},  []

    for c in str:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1

    for c, f in freq.items():
        heappush(heap, (-f, c))

    result = []
    while heap:
        f, c = heappop(heap)
        f = -f
        for _ in range(f):
            result.append(c)
            
    return "".join(result)


def main():

    print(
        "String after sorting characters by frequency: "
        + sort_character_by_frequency("Programming")
    )
    print(
        "String after sorting characters by frequency: "
        + sort_character_by_frequency("abcbab")
    )


main()
