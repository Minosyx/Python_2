import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy.random import rand, randn


lo = -8
up = 8
S = 1000
k = .1
a = .9
b = .04
c = .06						# parametry algorytmu roju


def f(x, y):
    obszar = np.logical_or(np.logical_or(x < lo, x > up), np.logical_or(y < lo, y > up))							# poza dziedziną
    return (2*np.cos(x+y)**2/(1+(x-y)**2/10)+np.sin(x-y)**3+0.5*np.sin(.6*x+y))*(1-obszar) + 1*obszar


x = lo+(up-lo)*rand(2, S)		# położenia cząstek w kolumnech
p = np.copy(x)				# najlepsze osiągnięcia cząstek w kolumnach
v = k*(up-lo)*randn(2, S)		# prędkości cząstek w kolumnach

X, Y = np.meshgrid(np.linspace(lo, up, 1000), np.linspace(lo, up, 1000))		# inicjalizacja siatki
# inicjalizacja figury - do animacji
fig, ax = plt.subplots(figsize=(12, 12), dpi=80)
ax.contourf(X, Y, f(X, Y), 100)												# wykres funkcji kolorami
# położenia cząstek na tle wykresu jako czarne punkty
line = ax.plot(x[0], x[1], '.k')[0]


def step():																	# krok algorytmu
    global g, v, x, p															# g - najlepsze osiągnięcie całego roju
    # indeks cząstki o najmniejszym minimum indywidualnym
    i = np.argmin(f(*p))
    g = p[:, i:i+1]                       										# minimum globalne
    # uaktualnienie prędkości cząstek
    v = a*v+b*rand(1, S)*(p-x)+c*rand(1, S)*(g-x)
    # uaktualnienie położenia na podstawie prędkości (dt = 1)
    x += v
    # uaktualniamy tablicę minimów indywidualnych
    p = np.array(list(zip(*[min(j, key=lambda i:f(*i))
                            for j in zip(p.T, x.T)])))


def animate(i):									# animacja - krok algorytmu i uaktualnienie położeń cząstek
    step()
    line.set_xdata(np.array(x[0]))
    line.set_ydata(np.array(x[1]))


fa = FuncAnimation(fig, animate, range(200), interval=200, repeat=False)
plt.show()
