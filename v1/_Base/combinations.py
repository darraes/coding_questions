def combination_i(array, start, depth, stack):
    #validations
    if depth < 0 or depth > len(array): raise
    if depth == 0:
        print stack
        return;
    else:
        for i in range(start, len(array)):
            stack.append(array[i])
            combination_i(array, i + 1, depth - 1, stack)
            stack.pop()

def combinations(array, size):
    combination_i(array, 0, size, [])

combinations([1, 2, 3, 4], 3)