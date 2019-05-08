from itertools import permutations

a = [1,2,3,4,5,6,7,8,9]
b = list(permutations(a))

c = []

for perm in b:
    d = perm[5]*1000 + perm[6]*100 + perm[7]*10 + perm[8]
    if((perm[0] * 100 + perm[1] * 10 + perm[2]) * (perm[3]* 10 + perm[4]) == d):
        if(d not in c):
            c.append(d)
    d = perm[5]*1000 + perm[6]*100 + perm[7]*10 + perm[8]
    if((perm[0] * 1000 + perm[1] * 100 + perm[2]*10 + perm[3]) * (perm[4]) == d):
        if(d not in c):
            c.append(d)
    
print(c)


            
total = 0
for i in c:
    total+=i
print(total)

