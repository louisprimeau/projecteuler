def Ma(n):
    a = []
    for i in range(0,n//2,1):
        a.append(i*i %n)
    print(n,end = ' ')
    print(max(a),end = ' ')
    print(a,end = ' ')
    print("")
    return(max(a))

sum = 0
for i in range(5,10**2 + 1,1):
    if(i % 100000 == 0):
        print(i // 100000)
    sum += Ma(i)
print(sum)
