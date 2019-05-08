iter = 0
lychrel = []
current = 0
def ispalindrome(i):
    if(str(i)[::-1] == str(i)):
        return True
    return False
for i in range(0,10000):
    iter = 0
    current = i
    while(iter < 50):
        current = current + int(str(current)[::-1])
        if(ispalindrome(current)):
            break
        if(iter == 49 and not(ispalindrome(current))):
            lychrel.append(i)
        iter += 1
print(lychrel)
print(len(lychrel))
    
        
