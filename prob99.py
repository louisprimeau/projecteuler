from math import log
lines = [line.rstrip('\n') for line in open('p099_base_exp.txt')]
a = []
for line in lines:
    b = line.split(',')
    a.append(log(int(b[0])) * int(b[1]))
biggest = 0
biggestindex = 0
for i in range(0,len(a)):
    if(biggest < a[i]):
        biggestindex = i
        biggest = a[i]

print(biggestindex)
    


