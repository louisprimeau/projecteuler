from sympy import divisor_count
def primechain(a,b):
    prime = True
    it = 0
    while(prime):
        if(divisor_count(it*it + it * a + b) == 2):
            it += 1
        else:
            prime = False
    return it

biggestchain = 0;
coefficients = [0,0]
primes = []
for b in range(-1000,1000):
    if(divisor_count(b) == 2):
           primes.append(b) 
            
for a in range(-1000,1000):
    for b in primes:
        c = primechain(a,b)
        if(biggestchain < c):
            biggestchain = c
            coefficients[0] = a
            coefficients[1] = b
            
print(coefficients[0])
print(coefficients[1])
print(coefficients[0] * coefficients[1])



