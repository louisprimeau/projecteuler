from itertools import permutations
from sympy import divisors
def isprime(int):
    if(int == 1):
        return False 
    if(len(divisors(int)) == 2):
        return True
    return False



a = [''.join(p) for p in permutations('1234567')]
for i in a:
    if(isprime(int(i))):
        print(i)
        
