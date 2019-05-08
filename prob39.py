#terrible brute force solution, probably double counts.
#It double counts everything, so it's cool. 
a = []
for i in range(0,1001):
    a.append(0)
for i in range(5,1000):
    for j in range(1, int((i - 2)/2) + 1):
        for k in range(1, j - 1):
            if(j**2 + k**2 == (i - j - k)**2):
                a[i] += 1
            elif((i - j - k)**2 + k**2 == j**2):
                a[i] += 1
            elif(j**2 + (i - j - k)**2 == k**2):
                a[i] += 1
print(a.index(max(a)))
                
