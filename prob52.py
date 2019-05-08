from itertools import permutations
a = []
for i in range(100000,1000000):
    a = [''.join(b) for b in permutations(str(i))]
    if(str(i*2) in a):
        if(str(i*3) in a):
            if(str(i*4) in a):
                if(str(i*5) in a):
                    if(str(i*6) in a):
                        print(i)
                        break
                    print(str(i) + " 5")
                print(str(i) + " 4")
            print(str(i) + " 3")
        print(str(i) + " 2")
