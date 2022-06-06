
from math import inf
for i in 'Ala':
    print(i)

it = iter('Ala')

while True:
    try:
        print(next(it))
    except StopIteration:
        break


class zakres:

    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            x = self.i
            self.i += 1
            return x
        raise StopIteration


for i in zakres(10):
    print(i)


class zakres1:

    def __init__(self, n):
        self.n = n

    def __getitem__(self, i):
        if i < self.n:
            return i
        raise IndexError


for i in zakres1(10):
    print(i)

print(iter(zakres1(10)))


class fib1:

    def __init__(self):
        self.before1 = 1
        self.before2 = 0

    def __iter__(self): return self

    def __next__(self):
        self.before1, self.before2 = (
            self.before1 + self.before2, self.before1)
        return self.before2


for x in fib1():
    if x > 100:
        break
    print(x)


class fib2:

    def __init__(self):
        self.before1 = 1
        self.before2 = 0

    def __getitem__(self, i):
        self.before1, self.before2 = (
            self.before1 + self.before2, self.before1)
        return self.before2


for x in fib2():
    if x > 100:
        break
    print(x)

###############################
print(40*'#')


def zakres2(n):		# funkcja generatora
    i = 0
    while i < n:
        yield i
        i += 1


z = zakres2(10)		# obiekt generatora
# for i in z:
#	print(i)

while True:
    try:
        print(next(z))
    except StopIteration:
        break


def fib_gen(n=inf):
    before1, before2 = (1, 1)
    while before2 < n:
        yield before2
        before1, before2 = before1 + before2, before1


def fib_gen(n=None):
    before1, before2 = (1, 1)
    warunek = (lambda x: True) if n == None else (lambda x: (x < n))
    while warunek(before2):
        yield before2
        before1, before2 = before1 + before2, before1


for i in fib_gen(100):
    print(i)

print(list(map((2).__mul__, range(10))))
