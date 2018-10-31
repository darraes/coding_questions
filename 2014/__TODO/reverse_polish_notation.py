# http://www.careercup.com/question?id=5762415492857856

import sys

# NOT WORKING
def rpn(str, start, end):
    if start > end: return 0
    if start == end:
        if str[start] == 'N': return 0
        else: return 1
    sub = str[start:end + 1]
    m = sys.maxint
    if str[end] == 'N':
        m = min(m, rpn(str, start, end - 1) + 1)

        for j in reversed(range(start, end)):
            m = min(m, 1 + rpn(str, j + 1, end) + rpn(str, start, j))
    else:
        for j in reversed(range(start, end - 1)):
            m = min(m,  rpn(str, j + 1, end - 1), rpn(str, start, j))

        m = min(m, rpn(str, start, end - 1) + 1)

    return m

def p_rpn(str):
    return rpn(str, 0, len(str) - 1)

#print p_rpn("NN*")
#print p_rpn("*NN*")
print p_rpn("NN*NN*")