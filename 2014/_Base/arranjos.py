#Solucao com DP.
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

ar = arranjo([1, 2, 3, 4], 2, 0)
print len(ar)
for a in ar:
    print a

#Solucao passando a subsolucao para o chamada seguinte
def arranjo2(array, used, size, current, buffer):
    if size == 0: 
        buffer.append(current[:])
        return

    for i in [j for j in range(len(array)) if not used[j]]:
        current.append(array[i])
        used[i] = True
        arranjo2(array, used, size - 1, current, buffer)
        used[i] = False
        current.pop()

buffer = []
arranjo2([1, 2, 3, 4], [False]*4, 3, [], buffer)
print len(buffer)
for a in buffer:
    print a



