input = "3+5*8*9+6+7"

result, acc, i = 0, 0, 0
while i < len(input):    
    if (input[i] == '+'):
        result = result + acc
        acc = 0
    elif (input[i] == '*'):
        while (True):
            i = i + 1
            if input[i] == '*': continue
            if input[i] == '+': break
            acc = acc * int(input[i])
        result = result + acc
        acc = 0
    else:
        acc = int(input[i])
    i = i + 1
result = result + acc

print result

##################################
result, acc, i = 0, 0, 0
while i < len(input):    
    if (input[i] == '+'):
        result = result + acc
        acc = 0
    elif (input[i] == '*'):
        while (input[i] == '*'):
            i += 1
            acc = acc * int(input[i])
            i += 1
        result = result + acc
        acc = 0
    else:
        acc = int(input[i])
    i = i + 1
result = result + acc

print result
            
