"""Project Euler 3"""

"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

#STRATEGY:
"""
The strategy is to start at the celing of the sqrt of the large number.
Then, at an odd number, test if divides, then test if prime. If this works,
break and we have the answer. Otherwise, decrement by 2."""

import math

def isPrime(n):  # Primality check.
    until=math.sqrt(n)+1
    for i in range(2,math.ceil(until)):
        if (n%i) == 0:
            return False
            break
    else:
        return True
            
def Euler3():
    bigN = 600851475143
    NSqrt = math.ceil(math.sqrt(bigN))
    if NSqrt%2==0: # Start at odd number
        NSqrt -=1
    while (bigN%NSqrt != 0 or (not isPrime(NSqrt))): #Tests divisor or prime
        NSqrt -= 2
    print(NSqrt)

Euler3()
