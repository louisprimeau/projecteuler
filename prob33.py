a = []
for i in range(10,100):
    for j in range(i+1,100):
        a.append((str(i),str(j)))
a1 = []
for b in a:
    c = b[0]
    if((c[0] in b[1]) or c[1] in b[1]):
        a1.append(b)
numerator = 1
denominator = 1
for b1 in a1:
    c = b1[0]
    d = b1[1]

    e = b1[0]
    f = b1[1]
    if(c[0] in b1[1]):
        d = d.replace(c[0], "", 1)
        c = c.replace(c[0], "", 1)
    elif(c[1] in b1[1]):
        d = d.replace(c[1], "", 1) 
        c = c.replace(c[1], "", 1)
     
    try:
        if((int(e)/int(f) == (int(c) / int(d))) and ('0' not in e)):
            print(c + "/" + d)
            numerator *= int(c)
            print(e + "/" + f)
            denominator *= int(d)
            print("----")
    except ZeroDivisionError:
        pass

print(numerator)
print(denominator)
