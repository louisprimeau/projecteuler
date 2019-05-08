def ispandigital(int):
    a = str(int)
    if('1' in a and '2' in a and '3' in a and '4' in a):
        if('5' in a and '6' in a and '7' in a and '8' in a):
            if('9' in a):
                return(True)
            else:
                return(False)


biggest = 0
for i in range(0,10000):
    a = ''
    for j in range(1,10):
        a += str(i * j)
        if(len(a) == 9):
            if(int(a) > biggest and ispandigital(int(a))):
                biggest = int(a)
            break
        if(len(a) > 9):
            break
print(biggest)
        
            
