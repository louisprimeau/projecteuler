from itertools import permutations

a = "0123456789"
b = [''.join(p) for p in permutations(a)]
total = 0
for i in b:
    if((int(i[1:4]) % 2 == 0) and (int(i[2:5]) % 3 == 0) and (int(i[3:6]) % 5 == 0) and (int(i[4:7]) % 7 == 0) and (int(i[5:8]) % 11 == 0)  and (int(i[6:9]) % 13 == 0) and (int(i[7:10]) % 17 == 0)):
        total += int(i)

print(total)
