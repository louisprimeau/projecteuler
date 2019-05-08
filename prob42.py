a = [all those words]
b = []
tn = []
wordvalue = 0
for c in a:
    for i in c:
        wordvalue += int(ord(i)) - 64
    b.append(wordvalue)
    wordvalue = 0
for i in range(0,100):
    tn.append((i * (i + 1))/2)
x = 0
for num in b:
    if(num in tn):
        x += 1
print(x)
    
