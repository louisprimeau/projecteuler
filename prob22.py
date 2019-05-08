a = [] #copy and paste text file here, too lazy to do file look up.
total = 0
namevalue = []
a.sort()
for b in a:
    for c in b:
        total += (ord(c) - 64)
    namevalue.append(total)
    total = 0
newtotal = 0
for x in range(0, len(namevalue)):
    newtotal += namevalue[x] * (x + 1)
print(len(a))
print(len(namevalue))
print(newtotal)
