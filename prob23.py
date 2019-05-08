from sympy import divisors
def divisorsum(int):
    total = 0
    c = divisors(int)
    c.pop(len(c) - 1)
    for a in c:
        total += a
    return total

abundants = []
for x in range(2,28123):
    if(divisorsum(x) > x):
        abundants.append(x)
total = 0

sums = set()
nums = set()
x = 0
for a in abundants:
    for b in abundants:
        x = a+b
        if (not(x in sums) and (x < 28123)):
            sums.add(x)
for x in range(0,28123):
    nums.add(x)

z = list(nums - sums)
for a in z:
    total += a
print(total)

