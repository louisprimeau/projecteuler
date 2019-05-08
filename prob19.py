months = [31,28,31,30,31,30,31,31,30,31,30,31]
day = 2
count = 0
years = 0
while(years != 100):
    if(years % 4 == 0):
        months[1] == 29
    else:
        months[1] == 28
    for i in range(0,len(months)):
        for j in range(1,months[i] + 1):
            
            if(day > 7):
                day = 1
            if(day % 7 == 0 and j == 1):
                count += 1
            day = day + 1
    years += 1
print(count)
