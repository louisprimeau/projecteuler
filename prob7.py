def isprime( x ):
    
    for i in range(2, x):
        if((x % i) == 0):
            return(False)
    return(True)
a = []
i = 2
while(len(a) < 10001):
    if(isprime(i) == True):
        a.append(i)
        print(i)
        print
    i += 1
print(len(a))
print(a[0])
print(a[10000])
