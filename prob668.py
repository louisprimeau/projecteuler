from itertools import permutations
from sympy.ntheory.factor_ import smoothness
from math import sqrt

smooth = 0;
for i in range(1,10**10 + 1,1):
    if(i%10**6 == 0):
        print(i//10**6)
    if(smoothness(i)[0] < sqrt(i)):
        smooth+=1

print(smooth + 1)
