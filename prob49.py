#Horrible brute force abomination:
from itertools import permutations
from sympy import divisors
def isprime(int):
    
    if(int == 1):
        return False 
    if(len(divisors(int)) == 2):
        return True
    return False
a = []
for i in range(1000,10000):
    if(isprime(i)):
        a.append(i)
for i in a: #over all primes
    for j in range(1000,5000): 
        b = i + j
        c = i + j + j
        if(isprime(b) and isprime(c) and (c < 9999)):
            a = set(str(i))
            b = set(str(b))
            c = set(str(c))
            if(a == b and b == c):
                print(i)
                print(j)
                #quit manually when you find it
                #me too thanks

