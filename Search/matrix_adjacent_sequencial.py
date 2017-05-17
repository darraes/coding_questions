# http://www.careercup.com/question?id=5147801809846272

"""Function"""
def get_adjacents(index, size):
    return [n for n in [(index[0] + 1, index[1]), \
                        (index[0] - 1, index[1]), \
                        (index[0], index[1] + 1), \
                        (index[0], index[1] - 1)] \
                        if n[0] >= 0 and n[0] < size and n[1] >= 0 and n[1] < size]

"""Function"""
def _find_max_sequence(matrix, cache, index, size):
    if cache.has_key(index): return cache[index]

    max_sequence = [matrix[index[0]][index[1]]]
    sub_max = []
    adjs = get_adjacents(index, size)
    for i in [i for i in adjs if matrix[i[0]][i[1]] - matrix[index[0]][index[1]] == 1]:
        sub_max = _find_max_sequence(matrix, cache, i, size)
        break

    max_sequence.extend(sub_max)
    cache[index] = max_sequence
    return max_sequence

"""Function"""
def find_max_sequence(matrix, size):
    max_sequence = []
    for i in range(size):
        for j in range(size):
            candidate = _find_max_sequence(matrix, dict(), (i, j), size)
            if len(candidate) > len(max_sequence):
                max_sequence = candidate

    return max_sequence



matrix = [[1, 4, 9],
          [2, 3, 8],
          [5, 6, 7]]

print find_max_sequence(matrix, 3)
        