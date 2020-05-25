from heapq import *


def rearrange_string(str):
    freq, heap = {}, []

    for n in str:
        if n not in freq:
            freq[n] = 0
        freq[n] += 1

    for c, f in freq.items():
        heappush(heap, (-f, c))

    result = []
    carry = None
    while heap:
        nf, c = heappop(heap)
        if carry:
            heappush(heap, carry)
            carry = None

        result.append(c)
        if -nf > 1:
            carry = (nf + 1, c)

    return "".join(result) if len(str) == len(result) else ""


def main():
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))


main()
