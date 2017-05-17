import math

def itoa(n):
    str = []
    while n > 0:
        str.append(chr(n%10 + ord('0')))
        n /= 10
    return str[::-1]
        


def ftoa(n):
    float_part = n

    decimals = 0
    while float_part != int(float_part):
        float_part *= 10
        decimals += 1

    str = itoa(int(float_part))
    l = len(str)
    print "{}.{}".format("".join(str[:(l-decimals)]), "".join(str[decimals + 1:]))

ftoa(123.44)


# Magnitude solution
def ftoa_top(n):
    str = ""
    m = int(math.log10(n))
    for i in range(5):    
        weight = 10**m
        digit1 = int(n / weight)
        n -= digit1*weight    
        str = str + "{}".format(digit1)
        if m == 0:
            str = str + "."
    
        m -=1
    return str

print ftoa_top(123.44)