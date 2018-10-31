def sink(stack, number):
    buffer = []

    while len(stack) > 0:
        element = stack.pop()
        if element < number:
            buffer.append(element)            
        else:
            stack.append(element)
            break

    stack.append(number)

    while len(buffer) > 0:
        stack.append(buffer.pop())

def sort(stack):
    if len(stack) < 1: return stack
    else:
        element = stack.pop()
        sort(stack)
        sink(stack, element)
        return stack


print sort([1, 4, 3, 7, 9, 5, 4])