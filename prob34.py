from numpy import math
total = 0
for i in range(0,100000):
    a = str(i)
    current = 0
    for x in a:
        current += math.factorial(int(x))
    if(current == i):
        total += i
        print(i)
        print(current)
print(total)
