max = 0
def digitsum(a):
    sum = 0
    for b in str(a):
        sum += int(b)
    return(sum)
for i in range(0,100):
    for j in range(0,100):
        a = i**j
        a = digitsum(a)
        if(a > max):
            max = a

print(max)
