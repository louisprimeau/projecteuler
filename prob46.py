from sympy import divisors
def isprime(int):
    if(int == 1):
        return False 
    if(len(divisors(int)) == 2):
        return True
    return False

primes = []
oddcomp = []
squares = []
a = []
for i in range(2,10000):
    if(isprime(i)):
        primes.append(i)
    elif(i % 2 != 0):
        oddcomp.append(i)

product = 1
for comp in oddcomp:
    for prime in primes:
        if(prime < comp):
            product *= ((((comp - prime)/2) ** (0.5)) % 1)
    if(product != 0):
        print(comp)
        break
    product = 1
        
