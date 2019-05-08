a = 1
b = 2
swap = 0
c = []
c.append(a)
while(b < 4000000):
    c.append(b)
    swap = a
    a = b
    b = swap + b
total = 0
for x in c:
    if((x % 2) == 0):
        total += x
print(total)
