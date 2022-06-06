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


class PseudoConnection:
    def __init__(self, x):
        self.x = x

    def send(self, y):
        pass

    def recv(self):
        return self.x


def obszar(T, Q, l, p, q, num):
    for _ in range(10000):
        l.send(T[1: -1, :1])
        p.send(T[1: -1, -1:])
        kolumnaL = l.recv()
        kolumnaR = p.recv()
        T[1:-1, :] = (T[:-2, :] + T[2:, :] + np.hstack((kolumnaL, T[1:-1, :-1])) +
                      np.hstack((T[1:-1, 1:], kolumnaR)) + dx**2 * Q[1:-1, :] / k) / 4
    q.put((num, T))


N = 4

Pipes = [list(mp.Pipe()) for _ in range(N-1)]
Ends = [PseudoConnection(T[1:-1, :1])] + list(sum(Pipes, [])) + [PseudoConnection(T[1:-1, -1:])]


q = mp.Queue()
lT = T.shape[0]

Processes = [mp.Process(target=obszar, args=(T[:, 1+i*(lT-2)//N:1+(i+1)*(lT-2)//N], Q[:, 1+i*(lT-2)//N:1+(i+1)*(lT-2)//N], Ends[2*i], Ends[2*i+1], q, i)) for i in range(N)]

for p in Processes:
    p.start()

T = np.concatenate([i[1] for i in sorted([q.get() for _ in range(N)])], axis=1)

plt.imshow(T)
plt.show()