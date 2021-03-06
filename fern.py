# Part C: Barnsely Ferns
import numpy as np
import matplotlib.pyplot as plt
#3a: Affine Functions

class AffineTransform(object):
    def __init__(self, a = 0, b = 0, c = 0, d = 0, e = 0, f = 0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def __call__(self,X):
        x,y = X
        point = [self.a*x + self.b*y + self.e, self.c*x + self.d*y + self.f]
        return point

#3b: Defining the functions
f1 = AffineTransform(c = 0.16)
f2 = AffineTransform(0.85, 0.04, -0.04, 0.85, 0, 1.60)
f3 = AffineTransform(0.20, -0.26, 0.23, 0.22, 0, 1.60)
f4 = AffineTransform(-0.15, 0.28, 0.26, 0.24, 0, 0.44)
functions = [f1, f2, f3, f4]

#3c: Non-uniform drawing
p1 = 0.01
p2 = 0.85
p3 = 0.07
p4 = 0.07
#probabilities = [p1,p2,p3,p4]      #Just to test sum
#print(sum(probabilities))
p_cumulative = [[0,0.01], [1,0.86], [2,0.93], [3,1]]
def randfunc():
    '''This will pick a random function.'''
    r = np.random.random()
    for j,p in p_cumulative:
        if r < p:
            return(functions[j])

#3d: Iterating the Fern
X = [0,0]
def iterate(X, n):
    '''Iterates the AffineTransform n times, currently prints out each point.'''
    Xlist = [X]
    for i in range(n):
        a = randfunc()
        X = a.__call__(X)
        Xlist.append(X)
    return(Xlist)
Xlist = iterate(X, 50000)

#3e: Plotting the Fern
plt.scatter(*zip(*Xlist), color = 'g', s = 0.8)
plt.axis('off')
plt.savefig('figures/barnsley_fern', dpi = 300, transparent = True)
