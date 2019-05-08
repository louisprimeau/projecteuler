a = []
for i in range(1,998):
    for j in range(i,1000 - i - 1):
        a.append([i,j,1000-i-j])

for b in a:
   b.sort()
   if(b[0] * b[0] + b[1] * b[1] == b[2] * b[2]):
       print(b[0] * b[1] * b[2])
