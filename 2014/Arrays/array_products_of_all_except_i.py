# http://www.careercup.com/question?id=5179916190482432

def products(array):
    result = [0] * len(array)

    before = [0] * len(array)
    after = [0] * len(array)

    before[0] = 1
    after[len(array) - 1] = 1

    for i in range(len(array)):
        if i >= 1:
            before[i] = array[i - 1] * before[i-1]

    for i in reversed(range(len(array))):
        if i < len(array) - 1:
            after[i] = array[i + 1] * after[i + 1]

    for i in range(len(array)):
        if i == 0:
            result[i] = after[i]
        elif i == len(array) - 1:
            result[i] = before[i]
        else:
            result[i] = before[i] * after[i]

    return result

print products([2,3,1,4])