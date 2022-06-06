
from math import cos, sin, pi


class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def r(self):
        return (self.x ** 2 + self.y ** 2) ** .5

    @r.setter
    def r(self, value):
        k = value / self.r
        self.x = k * self.x
        self.y = k * self.y

    @r.deleter
    def r(self):
        raise AttributeError('Nie można usuwać atrybutów w tej klasie')


"""
    def r_czytaj(self):
        return (self.x ** 2 + self.y ** 2) ** .5

    def r_zapisz(self, value):
        k = value / self.r
        self.x = k * self.x
        self.y = k * self.y

    def r_usun(self):
        raise AttributeError('Nie można usuwać atrybutów w tej klasie')

    r = property(r_czytaj, r_zapisz, r_usun, 'atrybut_r')
"""

p = Punkt(1, 2)
print(p.r)
p.r = 3
print(p.x, p.y)
print(p.r)
# del p.r


class Punkt2(Punkt):
    @Punkt.r.getter
    def r(self):
        return self.x


print(40*'#')

pa = Punkt2(1, 2)
print(pa.r)

# property tworzy deskryptor

# @property
# def r(self):
#     return (self.x ** 2 + self.y ** 2) ** .5

# print(dir(r))


class Deskryptor:
    def __get__(self, instancja, klasa):
        return (instancja.x ** 2 + instancja.y ** 2) ** .5

    def __set__(self, instancja, value):
        k = value / instancja.r
        instancja.x = k * instancja.x
        instancja.y = k * instancja.y

    def __delete__(*args):
        raise AttributeError('Nie można usuwać atrybutów w tej klasie')


class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    r = Deskryptor()


p = Punkt(1, 2)
print(p.r)
p.r = 10
print(p.r)

###############


class Klasa:
    @staticmethod
    def metoda_statyczna(*args):
        print(args)

    @classmethod
    def metoda_klasy(*args):
        print(args)

    def metoda(*args):
        print(args)


k = Klasa()
k.metoda_statyczna('a')
k.metoda_klasy('a')
k.metoda('a')
Klasa.metoda_statyczna("Kappa")
Klasa.metoda_klasy("no nieźle")


class Punkt3(Punkt):
    @classmethod
    def biegunowo(c, r, phi):
        x = r * cos(phi)
        y = r * sin(phi)
        return c(x, y)


p = Punkt3(1, 2)
p = Punkt3.biegunowo(1, pi/4)
print(p.x, p.y)