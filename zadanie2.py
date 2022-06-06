import numpy as np
from numpy.random import rand, randn
from math import inf


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


class NewMinimum(BaseException):
    pass


def particle(x, v):
    global better_p
    g = np.copy(x)
    p = np.copy(x)
    fmin = f(*p)
    while True:
        try:
            yield
        except NewMinimum as e:
            g = e.args[0]
        except GeneratorExit:
            break
        v = a*v+b*rand(2)*(p-x)+c*rand(2)*(g-x)
        x += v
        tmin = f(*x)
        if tmin < fmin:
            p = np.copy(x)
            fmin = f(*p)
            if fmin < f(*g):
                better_p.append(p)


g = np.zeros(2)
swarm = [particle(x=lo+(up-lo)*rand(2), v=k*(up-lo)*randn(2)) for _ in range(1000)]

for _ in swarm:
    _.send(None)

for _ in range(50):
    better_p = []
    for i in swarm:
        next(i)
    if better_p:
        g = min(better_p, key=lambda x: f(*x))
        for i in swarm:
            i.throw(NewMinimum(g))
print(g, f(*g))
