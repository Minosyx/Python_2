import numpy as np
import multiprocessing as mp
from time import time
import matplotlib.pyplot as plt


def f(Z):
    R = 255*np.ones(Z.shape)
    Z0 = np.copy(Z)
    for n in range(255):
        R[np.logical_and(R == 255, np.abs(Z) > 2)] = n
        Z = Z**2 + Z0
    return R


def mand(Z, q, num):
    q.put((num, f(Z)))


X = np.linspace(-2, 1, 301)
Y = np.linspace(-1.5, 1.5, 301)
X, Y = np.meshgrid(X, Y)
Z = X + 1j*Y

N = 4

q = mp.Queue()
obszary = np.array_split(Z, N, axis=1)

procesy = [mp.Process(target=mand, args=(obszary[i], q, i)) for i in range(N)]

for p in procesy:
    p.start()

#for p in procesy:
#    p.join()

r = [q.get() for _ in range(N)]
r.sort()
r = list(map(lambda i: i[1], r))
r = np.concatenate(r, axis=1)
plt.imshow(r)
plt.show()
