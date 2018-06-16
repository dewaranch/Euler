""" Euler 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""
"""Strategy:
Create a list to hold the primes.
create a counter
While the list holder has a length less than 10001,
add two to counter,
Then check if prime.
if prime, add to list"""

import math

def isPrime(n):
    until=math.sqrt(n)+1
    for i in range(2,math.ceil(until)):
       if (n%i) == 0:
           return False
           break
    else:
        return True

def Euler7():#could be made much faster using a sieve.
    holdlength=10001
    primes=[2,3]
    counter=3
    while len(primes)<holdlength:
        counter=counter+2
        if isPrime(counter):
            primes.append(counter)
    print(primes[-1])
    

Euler7()
