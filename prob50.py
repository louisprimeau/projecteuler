from itertools import permutations
from sympy import divisors #two wonderful libraries.




def isprime(int):
    if(int == 1):
        return False 
    elif(len(divisors(int)) == 2):
        return True
    return False
lprime = 999983
a = []
max = 0
for j in range(2,100,1):
    for i in range(j,10**4, 1):
        if(isprime(i)):
            a.append(i)
        suma = sum(a)
        if(isprime(suma) and suma < 1000000 and suma > max):
            max = suma
    a = []

print(max)
