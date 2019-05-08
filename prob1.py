
a = []
b = []
c = []
for i in range(1, 200):
    if((i % 3) != 0):
        a.append(5 * i)
for j in range(1, 334):
    a.append(3 * j)
total = 0
for element in a:
    total += element
print(total)
