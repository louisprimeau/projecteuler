from sympy import divisors
def isprime(int):
    if(int == 1):
        return False 
    if(len(divisors(int)) == 2):
        return True
    return False


def pdc(int):
    a = divisors(int)
    c = []
    for b in a:
        if(isprime(b)):
            c.append(b)
    return(len(c))

for i in range(0,1000000):
    if(pdc(i) == 4 and pdc(i+1) == 4 and pdc(i+2) == 4 and pdc(i+3) == 4):
        print(i)
        break

