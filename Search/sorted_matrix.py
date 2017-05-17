# http://www.careercup.com/question?id=5742801656479744

import math

def is_line_solved(line):
    for i in range(len(line) - 1):
        if line[i] > line[i+1]: return False
    return True


def is_matrix_solved(matrix):
    for row in matrix:
        if not is_line_solved(row): return False
    for column in zip(*matrix):
        if not is_line_solved(column): return False
    return True


def explode_internal(array, current, matrix, resultSet):
    if current == len(array) and is_matrix_solved(matrix):
        for row in matrix:
            print row
        print ""
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][j] = array[current]
                    explode_internal(array, current + 1, matrix, resultSet)
                    matrix[i][j] = 0


def explode(array):
    sroot = int(math.sqrt(len(array)))
    if (math.pow(sroot, 2) == len(array)):
        matrix = []
        for q in range(sroot):
            matrix.append([0]*sroot)
        resultSet = []
        explode_internal(array, 0, matrix, resultSet)
        return resultSet
    else:
        raise


explode([1, 2, 3, 4, 5, 6, 7, 8, 9]);



