def count_bits_to_convert(n, m):
    count = 0

    i = n ^ m
    while i > 0:
        count += i & 1
        i >>= 1

    return count