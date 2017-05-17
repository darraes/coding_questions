problem1 = [
          [1, 0, 0, 0, 6, 4, 5, 8, 0],
          [0, 4, 6, 0, 0, 0, 0, 0, 3],
          [0, 0, 0, 7, 3, 9, 4, 6, 0],
          [0, 0, 9, 1, 0, 2, 0, 0, 0],
          [2, 0, 0, 0, 5, 0, 0, 0, 9],
          [0, 0, 0, 3, 0, 7, 8, 0, 0],
          [0, 6, 2, 5, 7, 1, 0, 0, 0],
          [5, 0, 0, 0, 0, 0, 1, 2, 0],
          [0, 3, 1, 6, 2, 0, 0, 0, 4]
         ]

def rotate(matrix):
    layer = 0
    while layer < len(matrix) / 2:
        first = layer
        last = len(matrix) - layer - 1

        for i in range(first, last):
            offset = i - layer
            top = matrix[first][i]

            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top

        layer += 1

    return matrix


for r in problem1:
    print r
print ""
for r in rotate(problem1):
    print r