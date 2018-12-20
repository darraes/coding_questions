Size = 9
Squares = 3

######
#Prints the sudoku
######
def print_sudoku( sudoku ):
    for row in sudoku:
        print row
        
######
#Checks if the current sudoku is solved
######          
def is_solved( sudoku ):
    row = [0] * (Size + 1)
    column = [0] * (Size + 1)
    square = [0] * (Size + 1)
    #print_sudoku (sudoku)

    for x in range(Size):
        for y in range(Size):
            if sudoku[x][y] == 0: return False

            row[sudoku[x][y]] = row[sudoku[x][y]] + 1
            if (row[sudoku[x][y]] > 1): return False

            column[sudoku[y][x]] = column[sudoku[y][x]] + 1
            if (column[sudoku[y][x]] > 1): return False

        row = [0] * (Size + 1)
        column = [0] * (Size + 1)
    
    for xsqr in range(Squares):
        for ysqr in range(Squares):
            for x in range(Squares):
                for y in range(Squares):
                     if (sudoku[Squares * xsqr + x][Squares * ysqr + y] == 0): 
                         return False
                     square[sudoku[Squares * xsqr + x][Squares * ysqr + y]] \
                        = square[sudoku[Squares * xsqr + x][Squares * ysqr + y]] + 1
                     if (square[sudoku[Squares * xsqr + x][Squares * ysqr + y]] > 1): 
                         return False
            square = [0] * (Size + 1)     
    return True;

######
#Checks if the line, column and square relative to the passed x, y are solved
######
def is_partially_solved(sudoku, x, y ):
    row = [0] * (Size + 1)
    column = [0] * (Size + 1)
    square = [0] * (Size + 1)
    
    for i in range(Size):
        if sudoku[x][i] == 0: continue
        row[sudoku[x][i]] = row[sudoku[x][i]] + 1
        if (row[sudoku[x][i]] > 1): return False

    for i in range(Size):
        if sudoku[i][y] == 0: continue
        column[sudoku[i][y]] = column[sudoku[i][y]] + 1
        if (column[sudoku[i][y]] > 1): return False

    xsqr = int(x / Squares) * Squares
    ysqr = int(y / Squares) * Squares
    for i in range(Squares):
        for j in range(Squares):
            if sudoku[xsqr + i][ysqr + j] == 0: continue
            square[sudoku[xsqr + i][ysqr + j]] = square[sudoku[xsqr + i][ysqr + j]] + 1
            if (square[sudoku[xsqr + i][ysqr + j]] > 1): return False
            
    return True;
    
######
#creates a boolean map to track the numbers that are part of the problem
######
def puzzle_map( sudoku ):
    puzzle_map = []       
    for x in range(Size):
        puzzle_map.append([])
        for y in range(Size):
            if sudoku[x][y] == 0:
                puzzle_map[x].append(True)
            else:
                puzzle_map[x].append(False)
    return puzzle_map

######
# Advances the matrix index to the next available position.
# Returns a tuple with 3 values
# 1 - If it found a valid position
# 2, 3 - X and Y of the position
######
def advance( puzzle_map, index ):
    x, y = index[0], index[1]
    ox, oy = x, y

    #sets the very first next index
    if (y < Size - 1):
        y = y + 1
    else:
        y = 0
        x = x + 1
    
    while (x < Size):
        while (y < Size):
            if (puzzle_map[x][y]): return (True, x, y)
            y = y + 1 
        y = 0
        x = x + 1
    
    return (False, ox, oy)

######
# 
######
def backtrack( puzzle_map, index ):
    x, y = index[0], index[1]
    ox, oy = x, y

    #sets the very first previous index
    if (y > 0):
        y = y - 1
    else:
        y = Size - 1
        x = x - 1
    
    while (x >= 0):
        while (y >= 0):
            if (puzzle_map[x][y]): return (True, x, y)
            y = y - 1 
        y = Size - 1
        x = x - 1
    
    return (False, ox, oy)

######
#Does the backtracking to solve the sudoku
######
def solve( sudoku ):
    puzzleMap = puzzle_map(sudoku)
    adv, x, y = advance(puzzleMap, (0, -1))
    cansolve, loop = True, 0
    
    while(True):
        loop = loop + 1
        if (sudoku[x][y] < Size):
            sudoku[x][y] = sudoku[x][y] + 1
            partial = is_partially_solved(sudoku, x, y)
            if not partial: continue
            adv, x, y = advance(puzzleMap, (x, y))
        else:
            sudoku[x][y] = 0
            cansolve, x, y = backtrack(puzzleMap, (x, y))

        if (is_solved(sudoku)):
            print "Solved in {} iterations".format(loop)
            return True
        if (not cansolve): return False
        
    return sudoku   

#RUN
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

problem2 = [
       [5, 3, 0, 0, 7, 0, 0, 0, 0],
       [6, 0, 0, 1, 9, 5, 0, 0, 0],
       [0, 9, 8, 0, 0, 0, 0, 6, 0],
       [8, 0, 0, 0, 6, 0, 0, 0, 3],
       [4, 0, 0, 8, 0, 3, 0, 0, 1],
       [7, 0, 0, 0, 2, 0, 0, 0, 6],
       [0, 6, 0, 0, 0, 0, 2, 8, 0],
       [0, 0, 0, 4, 1, 9, 0, 0, 5],
       [0, 0, 0, 0, 8, 0, 0, 7, 9]
      ]

print solve(problem2)
print_sudoku (problem2)
