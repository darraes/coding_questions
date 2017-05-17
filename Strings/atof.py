def atof(str):
    sum = floating = count = 0
    after = False

    for i in range(len(str)):
        if str[i] == '.': 
            after = True
            continue

        if not after:
            sum *= 10
            sum += ord(str[i]) - ord('0')
        else:
            floating *= 10
            floating += ord(str[i]) - ord('0')
            count += 1

    return sum + (float(floating) / (10 ** count))

#No Overflow
def atof2(str):
    sum = floating = 0
    factor = 10.0

    for i in range(len(str)):
        if str[i] == '.': 
            factor = 0.1
            continue

        if factor == 10.0:
            sum *= factor
            sum += ord(str[i]) - ord('0')
        else:
            sum += (ord(str[i]) - ord('0')) * factor
            factor /= 10

    return sum

print atof("123.55")
print atof2("123.55")