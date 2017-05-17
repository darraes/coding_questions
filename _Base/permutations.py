def permute1(array, current, visited, buffer, result):
    if current > len(visited): 
        return
    if current == len(visited): 
        result.append([i for i in buffer])

    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            buffer[i] = array[current]
            permute1(array, current + 1, visited, buffer, result)
            visited[i] = False


def permute2(st, end, data):
    if st >= end - 1: return [[data[st]]]
    current = data[st]

    perms = []
    subperms = permute2(st + 1, end, data)
    for sp in subperms:
        for i in range(len(sp) + 1):
            set = []
            set.extend(sp[:i])
            set.append(current)
            set.extend(sp[i:])
            perms.append(set)

    return perms



print "PERMUTE 1"
perms = []
permute1([2, 9, 7], 0, [False] * 3, [0] * 3, perms)
for p in perms:
    print p

print "PERMUTE 2"
for p in permute2(0, 3, [2, 9, 7]):
    print p