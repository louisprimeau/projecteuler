list = []
for i in range(2, 10000000):
    a = str(i)
    total = 0
    for b in a:
        total += int(b)**5
    if(total == i):
        list.append(i)

total = 0
for c in list:
    total += c
print(total)
