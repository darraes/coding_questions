# http://www.careercup.com/question?id=6321181669982208

# Given a number N, write a program that returns all possible combinations of 
# numbers that add up to N, as lists. (Exclude the N+0=N) 

# For example, if N=4 return {{1,1,1,1},{1,1,2},{2,2},{1,3}}

def _add_up(number, array, start, selection):
    if number < 0: return;
    if number == 0:
        print selection
    else:
        for i in range(start, len(array)):
            selection.append(array[i])
            _add_up(number - array[i], array, i, selection)
            selection.pop()

def add_up(number):
    _add_up(number, range(1, number), 0, [])

add_up(10)

# This variation has an array as a list of possible values for the equation
def add_up_dp(number, choices, index):
    if index == len(choices) - 1:
        if number % choices[index] == 0: 
            return [[choices[index]] * (number / choices[index])]
        else: 
            return None

    result = []
    i = 0
    while i * choices[index] <= number:
        level = [choices[index]] * i
        sub_results = add_up_dp(number - i * choices[index], choices, index + 1)
        if sub_results is not None:
            for sub_result in sub_results:
                new = level[:]
                new.extend(sub_result)
                result.append(new)
        i += 1

    return result

for r in add_up_dp(10, [1,2,3], 0):
    print r
