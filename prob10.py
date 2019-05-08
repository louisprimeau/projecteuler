#a simple brute force approach
import math
def isprime( x ):
    
    for i in range(2, int(math.sqrt(x)) + 5):
        if((x % i) == 0):
            return(False)
    return(True)
a = [2,3,5]
for i in range(2, 2000000):
    if(isprime(i) == True):
        a.append(i)
      
total = 0
for i in a:
    total += i
print(total)




