"""Euler Project 4
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

"""
Could be made more efficient by starting at 999 and decrementing,
but run time is <1 second, so not really necessary.
"""

def IsPalindrome(n): #Tests if palindrome.
    return str(n) == str(n)[::-1]


def Euler4(): # Loops through 3 digit numbers, finds largest palindrome.
    Counter=0
    BigSoFar=0
    for i in range(100,999):
        for j in range(100,999):
            Counter= i*j
            if IsPalindrome(Counter):
                if Counter > BigSoFar:
                    BigSoFar=Counter
                    div1=i
                    div2=j
    print(str(BigSoFar)+" is " + str(div1) + " times "+str(div2))

Euler4()
