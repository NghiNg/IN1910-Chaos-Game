
import numpy as np
import matplotlib.pyplot as plt

c = [[0,0],[0,1],[np.sqrt(3)/2,1./2]]
x,y,z = c

plt.scatter([0,0,np.sqrt(3)/2],[0,1,1./2])
plt.axis('equal')
#plt.show()

def r(n):
    '''Creates a list of random numbers between [0,1).'''
    r = []
    for i in range(n):
        r.append(np.random.random())
    sum = 0
    for i in r:
        sum += i
    for i in range(n):
        r[i] = r[i]/sum
    return r

def points(n):
    R = r(3)
    points = []
    a = []
    for i in range(n):
        s = 0
        for j in range(3):
            a.append([[r[j]*k for k in l] for l in c])
        points.append(s)
    return points

x = []
y = []
points(2)
"""P = points(1000)
for i in range(1000):
    x.append(P[i][0])
    y.append(P[i][1])
plt.scatter(x,y)
plt.show()
"""
