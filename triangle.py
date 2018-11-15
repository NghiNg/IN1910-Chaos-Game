import numpy as np
import matplotlib.pyplot as plt

#Task 1.a
c = [(0,0),(0,1),(np.sqrt(3)/2,1./2)]
x,y,z = c
'''Create c triangle, plots manually'''
plt.scatter(*zip(*c))
plt.axis('equal')
#plt.show()

#Task 1.b
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
    '''Creates a random point inside the triangle'''
    R = r(3)
    a = []
    x = 0
    y = 0
    cc = np.copy(c)
    for i in range(3):
        for j in range(2):
            cc[i][j] = R[i]*c[i][j]
    for i in cc:
        x += i[0]
        y += i[1]
        point = (x,y)
    return point

def points(n):
    '''Creates a list of n random points in the triangle'''
    points = []
    for i in range(n):
        points.append(point())
    return points

'''
x = []
y = []
P = points(1000)
plt.scatter(*zip(*P))
plt.show()
'''

#Task 1.c
def halfling(n):
    X = np.array(point())
    #C = np.array(c[np.random.randint(3)])
    for i in range(6):
        X = (X + np.array(c[np.random.randint(3)]))/2
    Xlist = [X]
    for i in range(n-1):
        Xlist.append((Xlist[i] + np.array(c[np.random.randint(3)]))/2)
    return Xlist
Hermoine = halfling(10000)

#Task 1.d: Plotting the points
plt.scatter(*zip(*Hermoine), s = 0.2, color = 'red')
plt.axis('off')
marker = '.'
plt.show()
