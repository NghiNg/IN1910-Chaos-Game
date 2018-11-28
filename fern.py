# Part C: Barnsely Ferns

#3a: Affine Functions

class AffineTransform(object):
    def __init__(self, a = 0, b = 0, c = 0, d = 0, e = 0, f = 0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def __call__(self,x,y):
        point = [self.a*x + self.b*y + self.e, self.c*x + self.d*y + self.f]
        return point
'''
a = AffineTransform(1,2,3,4,5,6)
print(a.__call__(1,2))
'''
