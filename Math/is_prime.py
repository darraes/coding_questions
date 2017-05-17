#Primes after a point in the series are multiples of 6 +/-1. that is 31 = 30 + 1, 37 = 36 + 1 and so on. 
#So find the first number in 10 digits that is divisible by 6 and then from then on check 
#if no-1 or no+1 is prime. increment by 6 and do the same check until the prime count = 5

#Proof: 
#Checking a million primes is certainly energetic, but it is not necessary 
#(and just looking at examples can be misleading in mathematics). 
#Here is how to prove your observation: take any integer n greater than 3, and divide it by 6. That is, write

#n = 6q + r 

#where q is a non-negative integer and the remainder r is one of 0, 1, 2, 3, 4, or 5.

#If the remainder is 0, 2 or 4, then the number n is divisible by 2, and can not be prime.
#If the remainder is 3, then the number n is divisible by 3, and can not be prime.

#So if n is prime, then the remainder r is either

#1 (and n = 6q + 1 is one more than a multiple of six), or
#5 (and n = 6q + 5 = 6(q+1) - 1 is one less than a multiple of six).


import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False

def get_primes(number):
    for n in range(number):
        if is_prime(n):
            yield n

for p in get_primes(100):
    print p