#Islands in the stream

#001000
#101011
#111011
#000000
#000100
#000000

#Given the above matrix, write a function to count the number of
#islands. An island is composed of adjacent 1s. In the figure above,
#the number of islands are 3.


def _find_adjancents(matrix, i, j):
    left = (i - 1, j)
    right = (i + 1, j)
    up = (i, j - 1)
    down = (i, j + 1)
    
    result = []
    for adj in [left, right, down, up]:
        if adj[0] >= 0 and adj[0] < len(matrix) \
           and adj[1] >= 0 and adj[1] < len(matrix[0]):
               result.append(adj)
               
    return result


def _mark_island(matrix, i, j):
    # validations
    if matrix[i][j] == 1:
        matrix[i][j] = 2
        adjacents = _find_adjancents(matrix, i, j)
        for adj in adjacents:
            _mark_island(matrix, adj[0], adj[1])
    

def count_islands(matrix):
    # validations
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                result += 1
                _mark_island(matrix, i, j)
                
    return result

matrix = [
[0,0,1,0,0,0],
[1,0,1,0,1,1],
[1,1,1,0,1,1],
[0,0,0,0,0,0],
[0,1,0,1,0,0],
[0,0,0,0,0,0]
]

print count_islands(matrix)