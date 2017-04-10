""" Euler 9
A Pythagorean triplet is a set of three natural numbers, a < b < c,
for which, a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def IsPythag(a,b,c): # Helper function that tests if pythagorean triple.
    NumList=[a,b,c]
    Biggest= max(NumList)
    NumList.remove(Biggest)
    side1=(NumList[0])**2
    side2=(NumList[1])**2
    if side1 + side2 == Biggest**2:
        return True
    else:
        return False
    
"""Strategy: We know sum is 1000 and we know answer is unique.
Get all triples that sum to 1000.
test for pythag.
Stop when answer is found.
"""

def Euler9():
    for i in range(1,1000):
        for j in range(1,1000-i):
            k=1000-i-j
            if IsPythag(i,j,k):
                product=i*j*k
                return product
print(Euler9())
