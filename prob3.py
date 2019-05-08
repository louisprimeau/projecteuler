import math
x = 600851475143
factors = []

while(x > 1):
    for i in range(1, math.floor(math.sqrt(x))):
        if((x % i) == 0):
            factors.append(i)
            x = x / i
    
print(factors)
