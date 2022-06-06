import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

X = np.linspace(-2, 1, 301)
Y = np.linspace(-2, 2, 401)
X, Y = np.meshgrid(X, Y)
Z = X + Y * 1j

R = 255 * np.ones(Z.shape)
Z0 = np.copy(Z)

fig = plt.figure(figsize=(12, 9))
w = plt.imshow(R, vmin = 0, vmax = 255)

def anim(n):
    global Z
    R[np.logical_and(R == 255, np.abs(Z) > 2)] = n
    Z = Z**2 + Z0
    w.set_data(R)

a = FuncAnimation(fig, anim, frames = 256)
plt.show()
