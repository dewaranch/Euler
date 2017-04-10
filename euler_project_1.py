
## Euler Project 1

def ThrFiSum():
    sum = 0
    for i in range(1, 1000):
        if i%3==0 or i%5==0:
            sum = sum + i
    print(sum)

ThrFiSum()

      
