import math
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Clustering.csv")
X = df['x']
Y = df['y']

#X = [2, 2, 8, 5, 7, 6, 1, 4]
#Y = [10, 5, 4, 8, 5, 4, 2, 9]


#X = [5, 8, 3, 4, 3, 6, 6, 5]
#Y = [7, 4, 3, 4, 7, 7, 1, 5]

euclideanDistance = [[0 for ii in range(len(X))] for i in range(len(X))]


for i in range(len(X)):
    p1 = [X[i], Y[i]]
    for j in range(len(X)):
        distance = math.dist(p1, [X[j], Y[j]])
        euclideanDistance[i][j] = distance
        euclideanDistance[j][i] = distance
eps = 3.5
minPoint = 3
corePoint = []
underCorePoint = []
maybeBorderPoint = []
borderPoint = []
noisePoint = []


for i in range(len(X)):
    poinMaker = []
    corP = []
    for j in range(len(X)):
        if euclideanDistance[j][i] <= eps:
            poinMaker.append([X[j], Y[j]])
            if(euclideanDistance[j][i] == 0):
                corP = [X[j], Y[j]]

    #print(poinMaker)
    if(len(poinMaker) >= minPoint):
        underCorePoint.append(poinMaker)
        corePoint.append(corP)
    elif(len(poinMaker) == 1):
        for xx in poinMaker:
            noisePoint.append(xx)
        #noisePoint.append(poinMaker)
    else:
        #for xx in poinMaker:
         #   maybeBorderPoint.append(xx)
        maybeBorderPoint.append(poinMaker)
clustar = []
ii = 0

for checkBorderPoint in maybeBorderPoint:
    for cP in checkBorderPoint:
        ckr = 0
        for corPnt in underCorePoint:
            if(cP in corPnt):
                ckr = 0
                continue
            else:
                ckr = 1
                break
        if(ckr == 1):
            borderPoint.append(cP)




m = 0;
tmpCorePoint = corePoint
tmpUnderCorePoint = underCorePoint
#print(tmpUnderCorePoint)
while(tmpCorePoint):
    lateClaster = max(tmpUnderCorePoint)
    m = tmpUnderCorePoint.index(lateClaster)
    print(tmpUnderCorePoint)
    print(tmpCorePoint)
    #print(lateClaster)
    print(m)
    tmpUnderCorePoint.pop(m)
    tmpCorePoint.pop(m)
    print(tmpUnderCorePoint)
    print(tmpCorePoint)
    j = 0

    while(j<len(tmpCorePoint) and j>=0):
        #print(len(tmpCorePoint))
        if tmpCorePoint[j] in lateClaster:
            for x in tmpUnderCorePoint[j]:
                if x not in lateClaster:
                    lateClaster.append(x)
            tmpUnderCorePoint.pop(j)
            tmpCorePoint.pop(j)
            if j == 0:
                continue
            j -= 1
        else:
            j += 1
    clustar.append(lateClaster)
print(clustar)

print("Core Point: ")
print(corePoint)
print("Points of Udar Core Point: ")
print(underCorePoint)
print("Normal Cluster under core point: ")
print(clustar)
print("Border Point: ")
print(borderPoint)
print("Noise Point:")
print(noisePoint)
if noisePoint:
    clustar.append(noisePoint)
print("Final Cluster: ")
print(clustar)
print("Cluster size: ")
print(len(clustar))


colors = "bgrcmykw"
color_index = 0


for xx in clustar:
    for x,y in xx:
        plt.scatter(x, y, s=30, c=colors[color_index])
    color_index += 1

plt.show()
