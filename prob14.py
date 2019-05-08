highit = 0
thenumber = 0

for x in range(1,1000000, 2): #odd numbers make longer chains, since they immediately increase
    init = x
    value = x
    it = 1
    while(value != 1):
        if(value % 2 == 0):
            value /= 2
        else:
            value = value * 3 + 1
        it += 1
    if(highit < it):
        highit = it
        thenumber = init

print(thenumber)
