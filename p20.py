import matplotlib.pyplot as plt
from time import time
import multiprocessing as mp
import numpy as np


def f(Z):
    R = 255*np.ones(Z.shape)
    Z0 = np.copy(Z)
    for n in range(255):
        R[np.logical_and(R == 255, np.abs(Z) > 2)] = n
        Z = Z**2 + Z0
    return R


def mand(Z, R, l, p):
    R[l:p] = f(Z).flatten


X = np.linspace(-2, 1, 201)
Y = np.linspace(-1.5, 1.5, 301)
X, Y = np.meshgrid(X, Y)
Z = X + 1j*Y

N = 4

Rury = [mp.Pipe() for _ in range(4)]
obszary = [Z[i*//N:...,]]

procesy = [mp.Process(target=mand, args=(o, r, ))
           for o, r in zip(obszary, Rury)]

for p in procesy:
    p.start()

#for p in procesy:
#    p.join()

r = mp.Array('d', np.zeros(Z.shape).flatten) # flatten ustawia wiersz za wierszem
plt.imshow(r)
plt.show()
