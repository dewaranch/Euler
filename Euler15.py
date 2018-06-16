"""Euler15
Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

"""
One way to think of it is unique orderings of 20 R and 20 D.
Once the 20 R are put down, it's unique. So i believe it's just 40 choose 20.
So we can just use the choose function!
"""

"""Let's see how efficient it is"""
import math

print(math.factorial(40)/(math.factorial(20)*math.factorial(20)))
    
