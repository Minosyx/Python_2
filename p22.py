import numpy as np
import matplotlib.pyplot as plt

n = 251
dx = 1/n

T = 25*np.zeros((n, n)) #[K]
T[0, :] = 50
T[-1, :] = 50
T[:, 0] = 0
T[:, -1] = 0

Q = np.zeros((n, n))

for j in range(n//4, 3*n//4):  # zakres sinusa (dwie polowki)
    a = (j-n/4)/(n//2)*2*np.pi
    s = n//2 + int(n//4 * np.sin(a))
    Q[s-n//40:s+n//40, j] = 5e2 #[W/m^2]

k = 5.8e-2  #[W/K]

for _ in range(10000):
    T[1:-1, 1:-1] = (T[:-2, 1:-1] + T[2:, 1:-1] + T[1:-1, :-2] + T[1:-1, 2:] + dx**2 * Q[1:-1, 1:-1] / k) / 4

plt.imshow(T)
plt.show()
