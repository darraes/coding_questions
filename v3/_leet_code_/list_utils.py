def from_list(list):
    idx = 0
    while idx < len(list) - 1:
        list[idx].next = list[idx +1]
        idx += 1 
    return list[0]


def equals(l1, l2):
    if l1 is None and l2 is None:
        return True

    if l1 is None or l2 is None:
        return False

    if l1.val != l2.val:
        return False

    return equals(l1.next, l2.next)