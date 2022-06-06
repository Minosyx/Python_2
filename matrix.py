import math
import numpy as np

class Matrix:
    def __init__(self, a11, a22, a12):
        self.a11 = a11
        self.a22 = a22
        self.a12 = a12
        self.a21 = a12

    @property
    def tr(self):
        return self.a11 + self.a22

    @tr.setter
    def tr(self, value):
        scale = value / self.tr
        self.a11 *= scale 
        self.a22 *= scale
    
    @property
    def det(self):
        return self.a11 * self.a22 - self.a21 * self.a12

    @det.setter
    def det(self, value):
        if self.a12 == 0 or self.a21 == 0:
            raise ValueError("Macierz jest diagonalna!")
        scale = value - self.a11 * self.a22
        scale /= -(self.a12 * self.a21)
        scale = scale ** .5
        self.a12 *= scale
        self.a21 *= scale

    @classmethod
    def from_eigen(self, eival, angle):
        a1 = math.cos(angle / 180.0 * math.pi)
        a2 = math.sin(angle / 180.0 * math.pi)
        b1 = -a2
        b2 = a1
        V = np.array([[a1, b1], [a2, b2]])
        A = np.array([[eival[0], 0], [0, eival[1]]])
        revV = np.linalg.inv(V)
        res = (V.dot(A)).dot(revV)
        return self(res[0][0], res[1][1], res[0][1])

        

        

m = Matrix(2, 9, 3)

print(m.tr)
print(m.a11, m.a22, m.a12)

m.det = -2
print(m.det)
print(m.a11, m.a22, m.a12)

k = Matrix.from_eigen([5, -5], 60)
print(k.a11, k.a22, k.a12)