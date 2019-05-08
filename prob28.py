
counter = 1
total = 1
for x in range(1,501):
    counter += x*2
    total += counter
    counter += x*2
    total += counter
    counter += x*2
    total += counter
    counter += x*2
    total += counter
print(total)
