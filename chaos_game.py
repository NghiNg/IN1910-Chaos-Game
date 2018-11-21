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
    def plot_ngon(self):
        plt.scatter(*zip(*self.corners))
        plt.axis('equal')
        plt.show()
        plt.close()

a = ChaosGame(3)
b = ChaosGame(4)
c = ChaosGame(5)
d = ChaosGame(6)
e = ChaosGame(7)
f = ChaosGame(100)

a.plot_ngon()
b.plot_ngon()
c.plot_ngon()
d.plot_ngon()
e.plot_ngon()
f.plot_ngon()
