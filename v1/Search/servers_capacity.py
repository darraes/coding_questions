# http://www.careercup.com/question?id=6282171643854848

def check_capacity(servers, load, task, allocations):
    if task == len(load):
        print allocations
        return True

    for i in range(len(servers)):
        if load[task] <= servers[i]:
            servers[i] -= load[task]
            allocations[task] = i
            if check_capacity(servers, load, task + 1, allocations): 
                return True
            servers[i] += load[task]
            del allocations[task]

    return False

print check_capacity([8, 16, 8, 32], [18, 4, 8, 4, 6, 6, 8, 8], 0, dict())
print check_capacity([1, 3], [4], 0, dict())
print check_capacity([1, 3, 8], [4, 4, 2, 2], 0, dict())
print check_capacity([1, 3, 8], [4, 4, 2, 1], 0, dict())
print check_capacity([24, 8], [6, 6, 6, 6, 8], 0, dict())