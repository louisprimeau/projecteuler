import math as m
def ispent(x):
    if((1/6 + m.sqrt(0.25 + 6*x)/3) % 1 == 0):
        return(True)
    return(False)


a = []
for x in range(1,10000):
    a.append(x * (3 * x - 1) / 2)

i = 0
for x in a:
    i += 1
    if(i % 1000 == 0):
        print(i)
    for y in a:
        if(ispent(x+y) and ispent(x+2*y)):
            print(x)
            break
