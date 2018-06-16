"""Euler Poject 2"""

"""Each new term in the Fibonacci sequence is generated by
adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms."""

def Euler2():
    sum=2
    F1=1#first term
    F2=2#second term
    FCurrent=0
    while FCurrent <= 4000000:
        FCurrent=F1+F2
        F1 = F2
        F2= FCurrent
        if FCurrent%2==0:#only sum even terms
            sum += FCurrent
    print(sum)
        
Euler2()
