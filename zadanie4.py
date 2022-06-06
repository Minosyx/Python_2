@(pochodna := (lambda h: (lambda f: (lambda x: (f(x + h) - f(x)) / h))))(1e-5)
def f(x):
    return x**2


print([f(x) for x in range(-5, 5)])


def gradient(h):
    def dekorator(f):
        def f_gradient(*x):
            f0 = f(*x)
            g = []
            for i in range(len(x)):
                x1 = list(x)
                x1[i] += h
                g.append((f(*x1) - f0) / h)
            return g
        return f_gradient
    return dekorator


@gradient(1e-5)
def f(x, y):
  return x**2+y**2

@gradient(1e-5)
def g(x, y, z):
    return x**5 + y**3 + z**2

print(f(1, 1))
print(g(2, 1, 3))

import datetime

def debug(path):
    def dekorator(f):
        def f_debug(*args):
            with open(path, 'a') as p:
                s = datetime.datetime.now()
                p.writelines(f"{s}; {args}; {f(*args)}\n")
        return f_debug
    return dekorator


@debug('wynik.txt')
@gradient(1e-5)
def g(x, y, z):
    return x**5 + y**3 + z**2

@debug('wynik.txt')
@pochodna(2)
def f1(x):
    return x**3

g(2, 1, 3)
f1(5)
