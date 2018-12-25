from scipy import optimize
import numpy as np
import math

def intersectionArea(d,r):
#    y = np.sqrt(r**2 - d**2)
#    return 2*(r**2)*math.asin(y/r)-(y*x)
    # this is the formula I have, double check that it is correct.
    return 2*r*r*math.acos((d*d)/(2*d*r)) - 0.5*np.sqrt((-d+2*r)*(d)*(d)*(d+2*r))

# d^2 + y^2 = r^2
# d = sqrt(r^2 - y^2)
# y  sqrt(r^2 - d^2)


#find r for two circles with intersected area of 100 and distance of 10.
#optimize.fixed_point(circarea,10, args=(d))

# area value we want

A = float(100)

# radius we want (will be an array of values once I get this working)

r = float(10)


n = float(0.001) #working number for incrementing


inc = float(0.01)
dec=2 #decimal places of specificity
p = 1 #tolerance

while (abs(A - intersectionArea(n,r)) >= p):
    if (A - intersectionArea(n,r)) > p:
        n = n - inc
#      print(intersectionArea(n,r))
        print(n)
    elif ((A - intersectionArea(n,r)) < -1*p):
        n = n + inc
        print(A - intersectionArea(n,r))




print(n)
    
