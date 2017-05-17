# Facci's question

#(a,b) = find_breaks(list, new)

#if (a == b) // trata caso da insercao num no

#else 
#a->end = new->start; 
#a->next = new
#new->next = b
#b->start = new->end

#a insercao interna seria:
#c = new Node(a);
#a->end = new->start;
#a->next = new;
#new->next = c;
#c->start = new->end;

#o 'a' eh o primeiro no que
#a->start < new->start <= a->end

#o 'b' o primeiro que
#b->start <= new->end < b->end

class DNode(object):
    def __init__(self, start, end, value):
        self._start = start
        self._end = end
        self._value = value

        self._next = None


def update(logs, new_log):
    head = before = after = logs

    while before is not None:
        if before._start < new_log._start and new_log._start <= before._end:
            break
        before = before._next
    
    if before is not None:
        after = before
    while after is not None:
        if after._start <= new_log._end and new_log._end < after._end:
            break
        after = after._next

    if before == after:
        raise "Not Implemented"
    else:
        if before is not None:
            before._next = new_log
            before._end = new_log._start
        else:
            head = new_log
        if after is not None:
            new_log._next = after
            after._start = new_log._end

    return head


def print_dlist(node):
    str = ""
    while node is not None:
        str += "({}, {}, {})-> ".format(node._start, node._end, node._value)
        node = node._next
    print str

def sample():
    n1 = DNode(0, 15, 'a')
    n2 = DNode(15, 30, 'b')
    n3 = DNode(30, 40, 'c')

    n1._next = n2
    n2._next = n3

    return n1

#(0, 15, 'a') (15, 30, 'b') (30, 40, 'c')
#(10, 32, 'd')
#(15, 22, 'd')
#(15, 30, 'd')
#(20, 30, 'd')
#(40, 50, 'd')
#(0, 5, 'd')
#(16, 22, 'd')
print_dlist(sample())
print_dlist(update(sample(), DNode(10, 32, 'd')))
print_dlist(update(sample(), DNode(15, 22, 'd')))
print_dlist(update(sample(), DNode(15, 30, 'd')))
print_dlist(update(sample(), DNode(20, 30, 'd')))
print_dlist(update(sample(), DNode(40, 50, 'd')))
print_dlist(update(sample(), DNode(0, 5, 'd')))



        

            



