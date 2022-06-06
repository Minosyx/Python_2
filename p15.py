import matplotlib.pyplot as plt
import numpy as np
from time import time

X = np.linspace(-2, 1, 301)
Y = np.linspace(-2, 2, 401)
X, Y = np.meshgrid(X, Y)
Z = X + Y * 1j

"""
def func(z):
    z0 = z
    for n in range(255):
        if abs(z) > 2:
            return n
        z = z**2 + z0
    return 255

t = time()
res = np.array([[func(z) for z in wiersz] for wiersz in Z])
print(time() - t)
"""

"""
t = time()
R = 255 * np.ones(Z.shape)
Z0 = np.copy(Z)
for n in range(255):
    R[np.logical_and(R == 255, np.abs(Z) > 2)] = n
    Z = Z**2 + Z0
print(time() - t)
"""

@np.vectorize
def func(z):
    z0 = z
    for n in range(255):
        if abs(z) > 2:
            return n
        z = z**2 + z0
    return 255


t = time()
R = func(Z)
print(time() - t)

print(R)
plt.imshow(R)
plt.show()
