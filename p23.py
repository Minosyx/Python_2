import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp

n = 251
dx = 1/n

T = 25*np.zeros((n, n))  # [K]
T[0, :] = 50
T[-1, :] = 50
T[:, 0] = 0
T[:, -1] = 0

Q = np.zeros((n, n))

for j in range(n//4, 3*n//4):
    a = (j-n/4)/(n//2)*2*np.pi
    s = n//2 + int(n//4 * np.sin(a))
    Q[s-n//40:s+n//40, j] = 5e2  # [W/m^2]

k = 5.8e-2  # [W/K]

########################


def lewy(T, Q, p, q):
    for _ in range(10000):
        p.send(T[1: -1, -1:])
        kolumna = p.recv()
        T[1:-1, 1:] = (T[:-2, 1:] + T[2:, 1:] + T[1:-1, :-1] + np.hstack((T[1:-1, 2:], kolumna)) + dx**2 * Q[1:-1, 1:] / k) / 4
    q.put((0, T))


def prawy(T, Q, p, q):
    for _ in range(10000):
        p.send(T[1: -1, :1])
        kolumna = p.recv()
        T[1:-1, :-1] = (T[:-2, :-1] + T[2:, :-1] + np.hstack((kolumna, T[1:-1, :-2])) + T[1:-1, 1:] + dx**2 * Q[1:-1, :-1] / k) / 4
    q.put((1, T))


pL, pP = mp.Pipe()
q = mp.Queue()
ProcesL = mp.Process(target=lewy, args=(T[:, :n//2], Q[:, :n//2], pL, q))
ProcesP = mp.Process(target=prawy, args=(T[:, n//2:], Q[:, n//2:], pP, q))

ProcesL.start()
ProcesP.start()

T = np.hstack(i[1] for i in sorted([q.get() for _ in range(2)]))

plt.imshow(T)
plt.show()
