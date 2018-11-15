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
#halfling[n] = (x,y,color == 2)
def halfling(n):
    X = np.array(point())
    for i in range(6):
        C = np.random.randint(3)
        X = (X + np.array(c[C]))/2
    Xlist = [X]
    color = [C]
    for i in range(n-1):
        C = np.random.randint(3)    #Saves the random indice
        color.append(C)
        Xlist.append((Xlist[i] + np.array(c[C]))/2)
    return Xlist, color

#Task 1.d: Plotting the points
#Task 1.e: Adding Colour
Hermoine, color = halfling(10000)
red = []
blue = []
green = []
for i in range(len(color)):
    if color[i] == 0:
        red.append(Hermoine[i])
    elif color[i] == 1:
        blue.append(Hermoine[i])
    else:
        green.append(Hermoine[i])

plt.scatter(*zip(*red), s = 0.1, color = 'red')
plt.scatter(*zip(*blue), s = 0.1, color = 'blue')
plt.scatter(*zip(*green), s = 0.1, color = 'green')
plt.axis('off')
marker = '.'
plt.show()


def ironic(n):
    C0 = np.array(([1,0,0],[0,1,0],[0,0,1]))
    C = np.random.randint(3)
    arrrgh = np.array([np.random.random(), np.random.random(), np.random.random()])
    ron = []
    ron.append((C0[C] + arrrgh)/2)
    for i in range(n):
            arrrgh = np.array([np.random.random(),
            np.random.random(), np.random.random()])
            ron.append((ron[i] + arrrgh)/2)
    return ron

Ron = ironic(10000)

plt.scatter(*zip(*Hermoine), c = Ron, s = 0.1)
#plt.scatter(*zip(*blue),c=ron, s = 0.1, color = 'blue')
#plt.scatter(*zip(*green),c=ron, s = 0.1, color = 'green')
plt.axis('off')
plt.axis('equal')
marker = '.'
plt.show()
