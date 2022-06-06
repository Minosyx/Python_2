import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Process, Pipe, Queue

T = np.zeros((100, 100))
T[:, 0] = T[:, -1] = 0
T[0, :] = T[-1, :] = 50
N = 200
T = 25*np.ones((N, N))
dx = 1./N             # [m]
T[:, 0] = T[:, -1] = 0    # [C]
T[0, :] = T[-1, :] = 50   # [C]
k = 5.8e-2          # [W/K]
Q = np.zeros((N, N))
for j in range(N//4, 3*N//4):
  Q[int(N/2+N/10*np.sin(20.*(j-N/2)/N)), j] = 5e3*dx**2    # [W]

imax = 60000


def proces(T, Q, pl, pp, q, num):
  for i in range(imax):
    pl.send(T[1:-1, :1])     # wysyłamy lewy brzeg na lewo
    pp.send(T[1:-1, -1:])    # wysyłamy prawy brzeg na prawo
    T[1:-1, :] = (T[2:, :]+T[:-2, :]+np.hstack((T[1:-1, 1:], pp.recv())) +
                  np.hstack((pl.recv(), T[1:-1, :-1])) + Q[1:-1, :]/k)/4
  q.put((num, T))


class PseudoConnection:

  def __init__(self, x):
    self.x = x

  def send(self, y):
    pass

  def recv(self):
    return self.x


n = 4
pi = [PseudoConnection(T[1:-1, :1])]+sum([list(Pipe())
                                          for i in range(n-1)], [])+[PseudoConnection(T[1:-1, -1:])]
q = Queue()
pr = [Process(target=proces, args=(T[:, 1+i*(N-2)//n:1+(i+1)*(N-2)//n], Q[:,
              1+i*(N-2)//n:1+(i+1)*(N-2)//n], pi[2*i], pi[2*i+1], q, i)) for i in range(n)]
for p in pr:
  p.start()
l = sorted([q.get() for j in range(n)], key=lambda i: i[0])

plt.imshow(np.hstack([i[1] for i in l]))
plt.show()
