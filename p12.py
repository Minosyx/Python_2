from math import atan2

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattr__(self, name):
        if name == 'r':
            return (self.x ** 2 + self.y ** 2) ** .5
        elif name == 'a':
            return atan2(self.y, self.x)
        else:
            raise AttributeError


    # def r(self):
    #     return (self.x ** 2 + self.y ** 2) ** .5
    
    # def a(self):
    #     return atan2(self.y, self.x)

p = Punkt(1, 2)
# print(p.r(), p.a())
print('r' in p.__dict__, 'r' in Punkt.__dict__, 'r' in object.__dict__)
print(p.x, p.y, p.r, p.a)
print(hasattr(p, 'a'))

class Klasa:
    def __init__(self, x):
        self.x = x

    def __getattribute__(self, name):
        if name == 'x':
            # return object.__getattribute__(self, 'x')
            return super().__getattribute__('x')
        return name

    def __setattr__(self, name, value):
        if name == 'x':
            super().__setattr__(name, value)
        else:
            raise AttributeError('Nie można tworzyć nowych atrybutów w tej klasie')
    
    def __delattr__(self, name):
        raise AttributeError('Nie można usuwać atrybutów w tej klasie!')



k = Klasa(10)
print(k.x, k.y)
print(object.__dict__)

##########################


class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattr__(self, name):
        if name == 'r':
            return (self.x ** 2 + self.y ** 2) ** .5
        elif name == 'a':
            return atan2(self.y, self.x)
        else:
            raise AttributeError

    def __setattr__(self, name, value):
        if name == 'r':
            pass # przeskaluj x i y
        elif name == 'a':
            pass # obróc x i y
        else:
            super().__setattr__(name, value)
    
    def __delattr__(self, name):
        if name in ['x', 'y', 'r', 'a']:
            raise AttributeError('Nie można usuwać atrybutów w tej klasie')
    

class Klasa1:
    __y = 0
    def __init__(self):
        self.__x = 1

k = Klasa1()
print(k._Klasa1__x, k._Klasa1__y)


#############

class Klasa2:
    def __init__(self):
        self.__x = 1

    def x_czytaj(self):
        return 3 * self.__x

    def x_zapisz(self, value):
        if value > 0 and value < 1:
            self.__x = value
        else:
            raise ValueError
    
    def x_usun(self):
        raise AttributeError('Nie można usuwać atrybutów w tej klasie')

    x = property(x_czytaj, x_zapisz, x_usun, 'atrybut_x')


k = Klasa2()
print(k.x)

# przepisać punkt