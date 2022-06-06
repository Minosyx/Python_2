import numpy as np
import matplotlib.pyplot as plt


def f(m):   # funkcja fabryki
    def wew(x):  # domknięcie funkcji f
        return m*x**2+(2-m)*x+3
    return wew


print(f(2)(5))

def f(x):
    return x**n


n = 3
# print(f(2))


l = [lambda x, i=i: x**i for i in range(1, 21)]

print([f(2) for f in l])


####################
# def ogran(f):
#     def f_ogran(*args):
#         w = f(*args)
#         return -1 if w < -1 else 1 if w > 1 else w
#     return f_ogran

def ogran(lo, hi):
    def ogran_wew(f):
        def f_ogran(*args):
            w = f(*args)
            return lo if lo is not None and w < lo else hi if hi is not None and w > hi else w
        return f_ogran
    return ogran_wew


@ogran(-1, 2)  # składnia dekoratora
def f1(x):
    return .5*x


print([f1(x) for x in range(-5, 5)])
# print([f2(x) for x in range(-5, 5)])


def pochodna(h):
    def dekorator(f):
        def f_pochodna(x):
            return (f(x+h) - f(x)) / h
        return f_pochodna
    return dekorator


# @ogran(1, 2)
@pochodna(1e-5)
def f1(x):
    return x**2


@pochodna(1e-5)
@ogran(1, 2)
def f2(x):
    return x**2


print([f1(x) for x in range(-5, 5)])

X = np.linspace(-2, 2, 401)
plt.plot(X, list(map(f1, X)))
plt.plot(X, list(map(f2, X)))
plt.show()
