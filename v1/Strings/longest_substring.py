#Best
def longest_substring(strA, strB):
    matrix = [[0 for y in range(len(strB) + 1)] for x in range(len(strA) + 1)]
    max = (0, 0)

    for i in range(1, len(strA) + 1):
        for j in range(1, len(strB) + 1):
            if (strA[i - 1] == strB[j - 1]): 
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else: 
                matrix[i][j] = 0

            if matrix[i][j] == max[0] + 1:
                max = (matrix[i][j], i - matrix[i][j])

    print "Starts at {} with length {}".format(max[1], max[0])
    return matrix;