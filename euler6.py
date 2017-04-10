""" Euler 6
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.

"""
def Euler6(): # Simple math.
    Squares=0
    Sums=0
    for i in range(1,101):
        Squares += i
        Sums += (i**2)
    Squares=Squares**2
    Diff=Squares-Sums
    print(Diff)
Euler6()
