#another problem made easy by python

fact = 1
for x in range(1,101):
    fact *= x

total = 0
for x in str(fact):
    total += int(x)
print(total)
