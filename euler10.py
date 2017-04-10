""" Euler 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

""" I believe this could be made faster with a better isPrime function
and maybe using a Sieve. """

import math


def isPrime(n): # Prime checking helper function. Doesn't work for 1 and 2.
    until=math.sqrt(n)+1
    for i in range(2,math.ceil(until)):
       if (n%i) == 0:
           return False
           break
    else:
        return True

def Euler10():
    PrimeList=[2]
    for i in range(3,2000000):
        if isPrime(i):
            PrimeList.append(i)
    print(sum(PrimeList))

Euler10()
