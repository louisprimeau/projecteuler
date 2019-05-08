from math import factorial,ceil
total = 0
for i in range(1,101):
    for j in range(1, i-1):
        a = factorial(i) / (factorial(j) * factorial(i-j))
        if(a > 1000000):
            print(str(i) + " choose " + str(j))
            total = total + 1
print(total)
