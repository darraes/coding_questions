# http://www.careercup.com/question?id=5090137058836480

def divide(a, b):
    real, remain = divmod(a, b)
    decimal = []
    remainders = {}
    i = 0
    while remain != 0:
        if remain not in remainders:
            remainders[remain] = i
        else:
            decimal.insert(remainders[remain],'(')
            decimal.append(')')
            break

        remain *= 10
        digit, remain = divmod(remain, b)
        decimal.append(str(digit))
        i += 1

    return str(real) + '.' + ''.join(decimal)

print divide(22, 7)