from collections import deque

def find_swaps(number):
    #TODO validate
    result = []
    for i in range(len(number) - 1):
        for j in range(i + 1, len(number)):
            new_number = list(number)
            tmp = new_number[i]
            new_number[i] = new_number[j]
            new_number[j] = tmp
            result.append(new_number)
    return result

def find_max(number, k):
    queue = deque()
    queue.append((0, number))

    conflict_set = []
    while len(queue) > 0:
        c_k, current = queue.popleft()
        if c_k == k:
            conflict_set.append(current)
        else:
            for swap in find_swaps(current) :
                queue.append((c_k + 1, swap))
    
    max = 0
    max_list = []
    for swap in conflict_set:
        current = 0
        for i in range(len(swap)):
            current = 10*current + swap[i]

        if current > max:
            max = current
            max_list = swap

    return max_list

print find_max([7, 8, 9, 9], 2)