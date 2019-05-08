import pandas as pd
def containsorigin(a):
    if(sum(merge(merge(axes(a[0:2] + a[2:4]), axes(a[2:4] + a[4:6])), axes(a[4:6] + a[0:2]))) == 4):
        return(1)
    return(0)

def merge(a,b):
    for i in range(0,len(a),1):
        if(a[i] != 0):
            b[i] = 1
    return(b)

def axes(a):
    crossed = [0,0,0,0]
    if(a[2] != a[0]):
        slope = (a[3] - a[1]) / (a[2] - a[0])
    else:
        slope = 99999999999999999999

    if(slope != 0):
        yint = -1 * slope * a[0] + a[1]
        xint = (slope * a[0] - a[1]) / slope
    else:
        yint = -1 * slope * a[0] + a[1]
        xint = a[0]

    #POSITIVE X AXIS
    if((a[3] > 0 and a[1] < 0) or (a[3] < 0 and a[1] > 0)):
        if(xint > 0):
            crossed[0] = 1
        elif(xint < 0):
            crossed[1] = 1

    #POSTIVE Y AXIS
    if((a[2] > 0 and a[0] < 0) or (a[0] > 0 and a[2] < 0)):
        if(yint > 0):
            crossed[2] = 1
        elif(yint < 0):
            crossed[3] = 1

    return(crossed)

df = pd.read_csv("p102_triangles.csv")
df.astype(int)
triangles = 0
for i in range(0,len(df), 1):
    if(containsorigin(list(df.iloc[i,]))):
        triangles += 1
print(triangles)
