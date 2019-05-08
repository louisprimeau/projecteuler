
#uses the sympy divisor_count to efficiently get divisor numbers
from sympy import divisor_count

i = 1
t = 0

thenumber = 0
count = 1
while(True):
    t += i
    if(divisor_count(t) >= 500):
        thenumber = t
        break
    i += 1

print(thenumber)
