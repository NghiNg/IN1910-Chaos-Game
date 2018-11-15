
import numpy as np
import matplotlib.pyplot as plt

c = [[0,0],[0,1],[np.sqrt(3)/2,1./2]]
x,y,z = c

plt.scatter([0,0,np.sqrt(3)/2],[0,1,1./2])
plt.axis('equal')
plt.show()

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

def point():
    R = r(3)
    a = []
    x = 0
    y = 0
    cc = np.copy(c)
    for i in range(3):
        for j in range(2):
            #a.append(R[i]*c[i][j])
            cc[i][j] = R[i]*c[i][j]
    for i in cc:
        x += i[0]
        y += i[1]
        point = [x,y]
    return point

def points(n):
    points = []
    for i in range(n):
        points.append(point())
    return points
print(point())
print(points(2))

x = []
y = []
'''
P = points(1000)
for i in range(1000):
    x.append(P[i][0])
    y.append(P[i][1])
plt.scatter(x,y)
plt.show()
'''
