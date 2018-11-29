import nose.tools as nt
from chaos_game import ChaosGame
import numpy as np


def test_a():
    t = ChaosGame(3,-2.71828)
    assert isinstance(t, ChaosGame)
    t2 = ChaosGame(1,0.6)
    assert isinstance(t2, ChaosGame)

def test_b():
    t = ChaosGame(4,0.99999999)
    assert(t != None)

def test_c():
    t = ChaosGame(4,0.3)
    t.iterate(20)
    assert(t.n == 4 and t.r == 0.3)

def test_d():
    t = ChaosGame(16,np.pi/4)
    theta2 = 2*np.pi/16
    tol = 1E-15
    assert((t.theta-theta2) < tol)


'''
In test a we are purposefully testing to raise an error by
construcing an object of type ChaosGame with an r that is
less than 0.

'''
