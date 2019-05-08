def ispalindrome(a):
    if(a == a[::-1]):
        return(True)
    return(False)

total = 0
for i in range(0,1000000,1):
    
    if(ispalindrome(str(i)) and ispalindrome(str(bin(i))[2::])):
        print(i)
        total += i
print(total)
