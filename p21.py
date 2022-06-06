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

def mand(o, z):
    A[z[0]:z[1]] = f(o).flatten()

X = np.linspace(-2, 1, 201)
Y = np.linspace(-1.5, 1.5, 301)
X, Y = np.meshgrid(X, Y)
Z = X + 1j*Y

s = Z.shape
A = mp.Array('d', np.zeros(s).flatten())

N = 4

obszary = [Z[i*s[0]//N:(i+1)*s[0]//N,:] for i in range(N)]
zakresy = [(s[1]*(i*s[0]//N), s[1]*((i+1)*s[0]//N)) for i in range(N)]
procesy = [mp.Process(target=mand, args=(o, z))
        for o, z in zip(obszary, zakresy)]

for p in procesy:
    p.start()

for p in procesy:
    p.join()

plt.imshow(np.array(A).reshape(s))
plt.show()
