import multiprocessing as mp
import numpy as np
from time import time
import matplotlib.pyplot as plt

A = np.array(range(100)).reshape(10, 10)
# print(A)
print(A.flatten())

krotka = np.array_split(A, 2, axis=1)
print(krotka)
# B = np.concatenate(krotka, axis=1)
# print(B)

# print(np.hstack(krotka)) # to samo co concatenate z axis=1
# print(np.vstack(krotka))  # to samo co concatenate z axis=0

####################

p = mp.Pool()   # mozna podac liczbe podprocesow

# r = p.map((2).__rpow__,  range(100))
# l = range(10**9)
# t = time()
# r = p.map((2).__rpow__, l)
# print(time() - t)
# t = time()
# r = list(map((2).__rpow__, l))
# print(time() - t)

def f(Z):
    R = 255*np.ones(Z.shape)
    Z0 = np.copy(Z)
    for n in range(255):
        R[np.logical_and(R==255, np.abs(Z) > 2)] = n
        Z = Z**2+Z0
    return R

N = 4

X = np.linspace(-2, 1, 301)
Y = np.linspace(-2, 2, 401)
X, Y = np.meshgrid(X, Y)
Z = X + Y * 1j

t = time()
k = mp.Pool(N).map(f, np.array_split(Z, N, axis=0))
r = np.concatenate(k, axis=0)
print(time() - t)
plt.imshow(r)
plt.show()