# http://www.careercup.com/question?id=14974673

def _nuggets(count, box, used):
    if count == 0: return (True, [])
    if count < 0: return (False, [])

    next_box = 0
    if box == 20: next_box = 9
    elif box == 9: next_box = 6
    else: 
        if count % 6 == 0:
            return (True, [6]*(count / 6))
        else: 
            return (False, [])

    i = 0
    while box * i <= count:
        candidate = [box] * i
        sub_result, set = _nuggets(count - box * i, next_box, used)
        if sub_result: 
            set.extend(candidate)
            return (True, set)
        i += 1

    return (False, [])

def nuggets(count):
    return _nuggets(count, 20, [])


print nuggets(35)