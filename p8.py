from functools import wraps


def dekorator(f):
    @wraps(f)
    def nowa(*args):
        v = f(*args)
        print('ok')
        return v
    # nowa.__name__ = f.__name__
    # nowa.__doc__ = f.__doc__
    return nowa


@dekorator
def f(x):
    'To jest funkcja podwajająca'
    return 2*x


print(f(2))
print(f.__name__)
print(f.__doc__)

print(40*'#')

###############################


def dekorator_ok(K):
    class nowa(K):
        def ok(self):
            return 'ok'
    nowa.__name__ = K.__name__
    nowa.__doc__ = K.__doc__
    return nowa


@dekorator_ok
class Klasa:
    'Nasza klasa'
    pass


k = Klasa()
print(k.ok())
print(Klasa.__doc__)


def kk(K):
    class nowa(K):
        def __init__(*args):
            K.__init__(*args)
            print('Konstruktor zakończył działanie')
    nowa.__name__ = K.__name__
    nowa.__doc__ = K.__doc__
    return nowa


@kk
@dekorator_ok2 := lambda K: (type(K.__name__, (K,), {'ok': lambda self: 'ok', '__doc__': K.__doc__}))
class Klasa:
    'Nasza KKK klasa'

    def __init__(self):
        print('trwa inicjowanie nowo stworzonej klasy')


k = Klasa()
print(k.ok())
print(Klasa.__doc__)


def negacja(K):
    if not hasattr(K, '__neg__') and hasattr(K, '__sub__'):
        class nowa(K):
            __neg__ = lambda self: self - self - self
        return nowa
    else:
        print('Warning: __neg__ istnieje lub __sub__ nie istnieje!')
        return K


def negacja(K): return type(K.__name__, (K,), {'__neg__': lambda self: self - self - self, '__doc__': K.__doc__}) if not hasattr(K, '__neg__') and hasattr(K, '__sub__') else K

class Negacja:
    def __call__(self, K):
        if not hasattr(K, '__neg__') and hasattr(K, '__sub__'):
            class nowa(K):
                __neg__ = lambda self: self - self - self
            return nowa
        else:
            print('Warning: __neg__ istnieje lub __sub__ nie istnieje!')
            return K

negacja = Negacja() # żeby tworzyć nowe dekoratory przez dziedziczenie i przesłanianie

@negacja
class Klasa:
  def __init__(self, x):
    self.x = x

  def __str__(self):
    return str(self.x)

  def __sub__(self, drugi):
    return Klasa(self.x - drugi.x)


k = Klasa(12)
k1 = Klasa(16)
print(k - k1)
print(-k)


######################

from attr import attrs, attrib

@attrs
class Klasa1:
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y

    x = attrib(default = 0)
    y = attrib(default = 0)

kl = Klasa1(1, 2)
print(kl.x)

class MK:
    def __enter__(self):
        return 2 # f w bloku
    def __exit__(*args):
        print('Metoda __exit__ :', args)
        print('Działania czyszczące z finally')

with MK() as f:
    print(f)
    # print(f/0)


############

# Atrybuty funkcji

def f(x):
    f.n += 1
    return 2*x
f.n = 0

print(f(2), f(3), f(5), f.n)