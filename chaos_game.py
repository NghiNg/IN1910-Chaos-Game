import numpy as np

class ChaosGame(object):

    def __init__(self,n,r):
        if isinstance(n,int) and n >= 3:
            self.n = n
        else:
            raise Exception('n has to be an integer higher or equal to 3.')
        if isinstance(r,float) and r < 1 and r > 0:
            self.r = r
        else:
            raise Exception('r has to be a decimal between 0 and 1')
        self.gone = self._generate_ngon()
    def __call__(self):
        print('test')

    def _generate_ngon(self):
        theta = 2*np.pi/self.n
        theatre = [theta]
        corners = []
        for i in range(self.n-1):
            theatre.append(theatre[i]+theta)
        for i in range(self.n):
            corners.append([np.sin(theatre[i]), np.cos(theatre[i])])
a = ChaosGame(4,0.72828)
