def multorder(n):
    i = 1
    if(n % 5 == 0 or n % 2 == 0):
        return(0)
    while(True):
        if(((10**i) % n) == 1):
            return(i)
        i = i + 1

    return(0)

max = 0
for n in range(2,1000):
    if(multorder(n) > max):
        max = n
print(max)
