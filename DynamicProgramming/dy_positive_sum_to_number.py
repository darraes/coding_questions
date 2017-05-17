# http://www.careercup.com/question?id=15290675

def _parts(number, value):
    if value == 0: return [[]]
    if value == 1: return [[1]*number]

    next_value = value - 1

    combinations = []
    i = 0
    while i * value <= number:
        level_usage = [value] * i
        sub_combs = _parts(number - i * value, next_value)

        for sub_comb in sub_combs:
            sub_comb.extend(level_usage)
            combinations.append(sub_comb)
        i += 1

    return combinations

def parts(number):
    return _parts(number, number - 1)


 
def _count(number, value):
    if number == 0: return 1
    if value == 1: return 1

    next_value = value - 1

    sum = i = 0
    while value * i <= number:
        sum += _count(number - value * i, next_value)
        i += 1
    return sum

def count(number):
    return _count(number, number - 1)


print parts(10)
print count(10)