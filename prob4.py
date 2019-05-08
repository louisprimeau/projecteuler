a = []
for i in range(100,999):
    for j in range(i, 999):
        if(str(i*j) == str(i*j)[::-1]):
            a.append(i*j)

print(max(a))
        

