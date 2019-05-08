from sympy import divisors
def isprime(int):
    if(int == 1):
        return False 
    if(len(divisors(int)) == 2):
        return True
    return False

def circular(intr):
    a = str(intr)
    for x in range(0, len(a)):
        if not(isprime(int(a))):
            return False
        a = a[len(a) - 1] + a
        a = a[:-1]
    return True

a = []
for i in range(1,1000000):
    if(isprime(i)):
        a.append(i)
c = []
for b in a:
    if(circular(b) == True):
        c.append(b)
print(len(c))
