# http://www.careercup.com/question?id=5724382534041600

def gcd(x, y):    
    if (y == 0): return x;
    return gcd(y, x % y)

def is_factorial_divisible(f, x):
    for i in range(1, f + 1):
        turn = gcd(i, x)
        if turn > 1:
            x = x / turn;

    if x == 1: return True
    else: return False

print is_factorial_divisible(6, 8)