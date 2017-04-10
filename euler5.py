"""Euler Project 5
2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by
all of the numbers from 1 to 20?

"""

def EveDiv(n): # Divisibility test
    for i in range(11,21):
        if n%i ==0:
            continue                       
        else:
            return False
    return True

def Euler5():
    Count=2520
    while EveDiv(Count)==False:
        Count += 2520
    print(Count)
        
Euler5()

