import numpy as np
import matplotlib.pyplot as plt

class ChaosGame(object):

    def __init__(self, n, r = 0.5):
        if isinstance(n, int) and n >= 3:
            self.n = n
        else:
            raise Exception('n has to be an integer higher or equal to 3.')
        if isinstance(r, float) and r < 1 and r > 0:
            self.r = r
        else:
            raise Exception('r has to be a decimal between 0 and 1')
        self.gone = self._generate_ngon()
    def __call__(self):
        print('test')

    def _generate_ngon(self):
        self.theta = 2*np.pi/self.n
        theatre = [self.theta]
        self.corners = []
        for i in range(self.n-1):
            theatre.append(theatre[i] + self.theta)
        for i in theatre:
            self.corners.append([np.sin(i), np.cos(i)])
        return self.corners
    def plot_ngon(self):
        plt.scatter(*zip(*self.corners))
        plt.axis('equal')

    def _starting_point(self):
        '''Creates a random point inside the n-gon'''
        r = []
        for i in range(self.n):
            r.append(np.random.random())
        rsum = sum(r)
        for i in range(self.n):
            r[i] /= rsum
        a = []
        x = 0
        y = 0
        goner = np.copy(self.gone)
        for i in range(self.n):
            for j in range(2):
                goner[i][j] = r[i]*self.gone[i][j]
        for i in goner:
            x += i[0]
            y += i[1]
            point = (x,y)
        return point

    def iterate(self, steps, discard = 5):
        X = self._starting_point()
        for i in range(discard):
            C = np.random.randint(self.n)
            X = self.r*self.flies[i] + (1.-self.r)*self.gone[C]
        self.flies = [X]
        for i in range(steps-1):
            C = np.random.randint(self.n)    #Saves the random indice
            self.flies.append(self.r*self.flies[i] + (1.-self.r)*self.gone[C])
        return self.flies

    def show(self):
        plt.scatter(*zip(*self.flies), color = 'black')
        self.plot_ngon()
        plt.axis('equal')

a = ChaosGame(3,0.5)
'''
for i in range(1000):
    x,y = a._starting_point()
    plt.scatter(x,y)
'''
a.iterate(10)
a.show()
