tr = []
pe = []
he = []
for i in range(40756,1000000):
    tr.append(i * (i+1) / 2)
for i in range(0, 100000):
    pe.append(i * (3*i - 1) / 2)
    he.append(i * (2*i - 1))

for i in tr:
    if((i in pe) and (i in he)):
        print(i)
        break
