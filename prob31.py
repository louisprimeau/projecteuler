
#works better in c
total = 0

for onepound in range(0,3,1):
     for fiftypence in range(0,5,1):
        print(fiftypence)
        for twentypence in range(0,11,1):
            for tenpence in range(0,21,1):
                for fivepence in range(0,41,1):
                    for twopence in range(0,101,1):
                        for penny in range(0,201,1):
                            if(onepound * 100 + fiftypence * 50 + twentypence * 20 + tenpence * 10 + fivepence * 5 + twopence * 2 + penny == 200):
                                total += 1
                            
print(total + 1)
