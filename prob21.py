from sympy import divisors

def divisorsum( int ):
    a = divisors( int )
    a.pop(len(a) - 1)
    total = 0
    for element in a:
        total += element
    return(total)


total = 0
for i in range(2,10000):
        if((divisorsum(divisorsum(i)) == i) and (divisorsum(i) != i)):
            total += divisorsum(i)
            total += i


print(total / 2)
