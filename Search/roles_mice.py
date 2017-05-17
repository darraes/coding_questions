# http://www.careercup.com/question?id=5146233651855360

def arranjo(array, size, start):
    if size == 1: return [[i] for i in array[start:]]

    result = []
    for i in range(start, len(array)):
        current = array[i]
        sub = arranjo(array, size - 1, i + 1)
        for s in sub:
            for j in range(size):
                temp = []
                temp.extend(s)
                temp.insert(j, current)
                result.append(temp)

    return result

def least_time(mices, holes):
    perms = []
    shortPerm = []
    shortTime = 100
    perms = arranjo(holes, len(mices), 0)
    for perm in perms:
        time = 0;
        for i in range(len(mices)):
            time = max (abs(mices[i] - perm[i]), time)
        if (time < shortTime):
            shortPerm = perm
            shortTime = time
    return shortTime, shortPerm

print least_time([4, -4, 2], [4, 5, 0])


