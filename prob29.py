a = set()
for i in range(2,101):
    for j in range(2,101):
        b = i**j
        if not(b in a):
            a.add(b)
print(len(a))
