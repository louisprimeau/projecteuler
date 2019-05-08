ones = ['','one','two','three','four','five','six','seven','eight','nine']
teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
hundred = 'hundred'

def digit(x,i):
    return(int(str(x // 10**i)[len(str(x // 10**i)) - 1]))

length = 0
namestring = ''
for i in range(1,1000,1):
    if(digit(i,2) != 0):
        namestring += (ones[digit(i,2)] + hundred)
        if(digit(i,1) != 0 or digit(i,0) != 0):
            namestring += 'and'
    
    if(digit(i,1) == 1 and digit(i,0) != 0):
        namestring += teens[digit(i,0)]
    else:
        namestring += tens[digit(i,1)]
        namestring += ones[digit(i,0)]
    length += len(namestring)
    print(namestring,end = ' ')
    print(len(namestring))
    namestring = ''

print(length)
print(len('onethousand'))
print(length + len('onethousand'))
    
