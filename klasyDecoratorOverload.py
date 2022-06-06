
def power(K):
    if not hasattr(K, '__pow__') and hasattr(K, '__mul__'):
        def p(x, n):
            if n < 1:
                return x / p(x, -n + 1)
            elif n == 1:
                return x
            elif n % 2:
                a = p(x, (n - 1) / 2)
                return x * a * a
            a = p(x, n / 2)
            return a * a
        K.__pow__ = p
        return K
    else:
        return K


@power
class Liczba:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return str(self.n)
        
    def __mul__(self, drugi):
        if isinstance(drugi, Liczba):
            return Liczba(self.n * drugi.n)
        elif isinstance(drugi, int):
            return Liczba(self.n * drugi)
    
    def __truediv__(self, drugi):
        if isinstance(drugi, Liczba):
            return Liczba(self.n / drugi.n)
        elif isinstance(drugi, int):
            return Liczba(self.n / drugi)

a = Liczba(5)

print(a**-3)

def multiply(K):
    if not hasattr(K, '__mul__') and hasattr(K, '__add__'):
        def f(x, n):
            if n < 1:
                return x - f(x, -n + 1)
            if n == 1:
                return x
            elif n % 2:
                a = f(x, (n - 1) / 2 )
                return x + a + a
            a = f(x, n / 2)
            return a + a 
        K.__mul__ = f
        return K
    else:
        return K


@multiply
class Liczba:
    def __init__(self, x):
        self.x = x
    
    def __str__(self):
        return str(self.x)

    def __add__(self, drugi):
        if isinstance(drugi, Liczba):
            return Liczba(self.x + drugi.x)
        elif isinstance(drugi, int):
            return Liczba(self.x + drugi)

    def __sub__(self, drugi):
        if isinstance(drugi, Liczba):
            return Liczba(self.x - drugi.x)
        elif isinstance(drugi, int):
            return Liczba(self.x - drugi)

a = Liczba(3)

print(a * -2)
