# http://www.careercup.com/question?id=5998719358992384

#Given a matrix consisting of 0's and 1's, find the largest connected component consisting of 1's.

from collections import deque

def adjacents(matrix, x, y):
    return [point for point in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] \
        if point[0] >= 0 and point[0] < len(matrix) and point[1] >= 0 and point[1] < len(matrix[0])]

def _calculate_size(matrix, x, y):
    size = 0    
    queue = deque()
    queue.append((x, y))
    matrix[x][y] = 2

    while len(queue) > 0:
        current = queue.popleft()                
        size += 1

        adjs = adjacents(matrix, current[0], current[1])
        for point in [point for point in adjs if matrix[point[0]][point[1]] == 1]:
            matrix[point[0]][point[1]] = 2
            queue.append(point)

    return size

def calculate_size(matrix):
    max_size = 0

    #To avoid changing the original matrix, we can clone it here

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                current_size = _calculate_size(matrix, i, j)
                if current_size > max_size: 
                    max_size = current_size

    return max_size


matr = [[1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 1, 0, 0, 1, 1, 1, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 1]]

print calculate_size(matr)

