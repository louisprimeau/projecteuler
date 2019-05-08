a = [1,20,190,1140,4845,15504,38760,77520,125970,167960,184756,167960,125970,77520,38760,15504,4845,1140,190,20,1] #20th pascal row
total = 0

for b in a:
    total += b**2
print(total) #sum of squares pattern found through inspection of lower cases
