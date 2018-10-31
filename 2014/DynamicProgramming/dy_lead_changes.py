# Question http://www.careercup.com/question?id=5659765149532160

# BEST SOLUTION
def improved_dp(high, low, points, cache):
    if high == 0 and low == 0: return 0
    if high < 0 or low < 0: return -1

    if cache.has_key((high, low)): return cache[(high, low)]

    current_max = 0
    for point in points:
        new_score = high - point

        max_so_far = 0
        if new_score <= low:
            max_so_far = improved_dp(low, new_score, points, cache) + 1
        else:
            max_so_far = improved_dp(new_score, low, points, cache)

        if max_so_far > current_max: 
            current_max = max_so_far

    cache[(high, low)] = current_max
    return current_max


def improved_dp_path(high, low, points, cache):
    if high == 0 and low == 0: 
        return 0, [(0, 0)]
    if high < 0 or low < 0: 
        return -1, [(0, 0)]

    if cache.has_key((high, low)): return cache[(high, low)]

    current_path = []
    current_max = 0
    for point in points:
        new_score = high - point

        max_so_far, path = 0, []
        if new_score <= low:
            max_so_far, path = improved_dp_path(low, new_score, points, cache)
            max_so_far += 1
        else:
            max_so_far, path = improved_dp_path(new_score, low, points, cache)

        if max_so_far > current_max: 
            current_max = max_so_far
            current_path = path[:]
            current_path.append((high, low))

    cache[(high, low)] = current_max, current_path
    return current_max, current_path



# Problem variation
# Missing DP Cache
def find_all_paths(score, points):
    if score == (0, 0): return [[(0, 0)]]
    if score[0] < 0 or score[1] < 0: return None

    paths = []

    for point in points:
        x_scores = find_all_paths((score[0] - point, score[1]), points)
        y_score = find_all_paths((score[0], score[1] - point), points)

        if x_scores is not None:
            for s in x_scores:
                s.append(score)
                paths.append(s)

        if y_score is not None:
            for s in y_score:
                s.append(score)
                paths.append(s)

    return paths


print improved_dp(100, 69, [2, 3], dict())
print improved_dp_path(100, 69, [2, 3], dict())
print improved(10, 6, [2, 3], 0)
for o in find_all_paths((6, 2), [2, 3]): print o


# OLD Code
#def down_lead_change(score, available, count):
#    change = 0
#    no_change = 1
#    receiver = []

#    if score[1] > score[0]: 
#        change = 1
#        no_change = 0

#    for point in available:
#        changing = score[change] - point
#        other = score[no_change]

#        if changing == 0 and other == 0: 
#            receiver.append(count + 1)
#            continue
#        if point == 0 or changing < 0 or other < 0:
#            continue

#        changes = 0
#        if (changing <= other):
#            changes = down_lead_change((changing, other), available, count + 1)            
#        else:
#            changes = down_lead_change((changing, other), available, count)

#        if (changes >= 0): receiver.append(changes)

#    receiver.append(-1)
#    return max(receiver)


#def up_lead_change(score, available):
#    receiver = []
#    if score[0] == 0 and score[1] == 0: return 0
#    if score[0] < 0 or score[1] < 0: return -1

#    bigger = score[0]
#    smaller = score[1]

#    if smaller > bigger: 
#        smaller = score[0]
#        bigger = score[1]

#    for point in available:
#        if point == 0: continue

#        result = bigger - point
#        if(result < 0): continue

#        inc = 0
#        if (result <= smaller): inc = 1

#        changes = up_lead_change((result, smaller), available)
#        if (changes != -1): receiver.append(changes + inc)

#    receiver.append(-1)
#    return max(receiver)