from sympy import divisors

def isprime(int):
    if(int == 1):
        return False 
    if(len(divisors(int)) == 2):
        return True
    return False

a = []
for i in range(10,1000000):
    if(isprime(i)):
        a.append(i)
b = ""
total = 0
for i in a:
    prime = True
    b = str(i)
    for j in range(0, len(b)):
        if not(isprime(int(b[0:j+1]))):
            prime = False
            if(prime == False):
                break
        if not(isprime(int(b[j:len(b)]))):
            prime = False
            if(prime == False):
                break
    if(prime == True):
        total += i
        print(i)
print(total)
        

