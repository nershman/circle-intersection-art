from scipy import optimize
import numpy as np
import math

def intersectionArea(d,r):
#    y = np.sqrt(r**2 - d**2)
#    return 2*(r**2)*math.asin(y/r)-(y*x)
    # this is the formula I have, double check that it is correct.
    return 2*r*r*math.acos((d)/(2*r)) - 0.5*np.sqrt((-d+2*r)*(d)*(d)*(d+2*r))

# d^2 + y^2 = r^2
# d = sqrt(r^2 - y^2)
# y  sqrt(r^2 - d^2)


#find r for two circles with intersected area of 100 and distance of 10.
#optimize.fixed_point(circarea,10, args=(d))

# area value we want

A = float(100)

# radius we want (will be an array of values once I get this working)

r2 = float(10)


#n = float(0.001) #working number for incrementing


#inc = float(0.01)
incstart = float(2)
incc = float(0.5)
dec=2 #decimal places of specificity
p = 0.1 #tolerance

#better seed value, using limitation of arccos
# d <= 2r
#n = (3*r2*r2) - r2
n = 1.5*r2
i=0
#two booleans. when the alg has gone too far in one direction, incrememnts become smaller
pos = False
neg = False

while (abs(A - intersectionArea(n,r2)) >= p):
    if neg == True & pos == True:
        pos = False
        neg = False
        incc = incc*incc
    elif (A - intersectionArea(n,r2)) > p:
        n = n - incstart*incc
        neg = True
        print(intersectionArea(n,r2),"too big")
#        print(n)
    elif ((A - intersectionArea(n,r2)) < -1*p):
        n = n + incstart*incc
        pos =True
        print(A - intersectionArea(n,r2),"too small")




print(n)
    
