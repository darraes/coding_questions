# http://www.careercup.com/question?id=4859932243394560

def print_subsets_internal(source, index, stack):
    sLength = len(source)

    if index == sLength: 
        print stack
    else:
        print_subsets_internal(source, index + 1, stack)
        stack.append(source[index])
        print_subsets_internal(source, index + 1, stack)
        stack.pop()


def print_subsets(source):
    print_subsets_internal(source, 0, [])


print_subsets("abc")