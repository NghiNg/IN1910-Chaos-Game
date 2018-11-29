import numpy as np
import matplotlib.pyplot as plt

#Task 1.a
c = np.array([(0,0),(0,1),(np.sqrt(3)/2,1./2)])
x,y,z = c
'''Create c triangle, plots manually'''
#plt.scatter(*zip(*c))
#plt.axis('equal')
#plt.show()

#Task 1.b
def r(n):
    '''Creates a list of random numbers between [0,1).'''
    r = []
    for i in range(n):
        r.append(np.random.random())
    for i in range(n):
        r[i] = r[i]/sum(r)
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

def halfling(n):
    X = np.array(point())
    #This is the first 5 that are discarded.
    for i in range(6):
        C = np.random.randint(3)
        X = (X + c[C])/2
    Xlist = [X]
    color = [C]
    RGB = np.array(([1,0,0],[0,1,0],[0,0,1]))
    arrrgh = np.array([np.random.random(), np.random.random(), np.random.random()])
    ron = [(RGB[C] + arrrgh)/2]
    for i in range(n-1):
        C = np.random.randint(3)    #Saves the random indice
        Xlist.append((Xlist[i] + c[C])/2)   #Creates the list of points.
        color.append(C)                     #Creates the basic color list.
        ron.append((ron[i] + RGB[C])/2)     #Creates the alternative color list.
    return Xlist, color, ron

Hermoine, color, Ron = halfling(10000)

red = []
green = []
blue = []
for i in range(len(color)):
    if color[i] == 0:
        red.append(Hermoine[i])
    elif color[i] == 1:
        green.append(Hermoine[i])
    else:
        blue.append(Hermoine[i])

#Plotting normal colours as task 1e.
plt.scatter(*zip(*red), s = 0.1, color = 'red')
plt.scatter(*zip(*green), s = 0.1, color = 'green')
plt.scatter(*zip(*blue), s = 0.1, color = 'blue')
plt.axis('off')
plt.axis('equal')
marker = '.'
plt.show()
#Plotting alternative colours with the corners as task 1f.
plt.scatter(*zip(*Hermoine), c = Ron, s = 0.1)
plt.axis('off')
plt.axis('equal')
marker = '.'
plt.show()
