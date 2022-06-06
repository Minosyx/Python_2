from math import inf
for i in 'Ala':
    print(i)

it = iter('Ala')

while True:
    try:
        print(next(it))
    except StopIteration:
        break


# for i in range(10**6):  # python2 robil liste
#     pass

class Zakres:
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


for i in Zakres(10):
    print(i)


class Zakres1:
    def __init__(self, n):
        self.n = n

    def __getitem__(self, i):
        if i < self.n:
            return i
        raise IndexError


for i in Zakres1(10):
    print(i)

print(iter(Zakres1(10)))


class fib:
    def __init__(self, n):
        self.n = n
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.n:
            raise StopIteration
        return self.a


for i in fib(25):
    print(i)


class fib1:
    def __init__(self, n):
        self.n = n
        self.a = 0
        self.b = 1

    def __getitem__(self, i):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.n:
            raise StopIteration
        return self.a


for i in fib1(25):
    print(i)


#########################
print(40*'#')


def zakres2(n):
    i = 0
    while i < n:
        yield i
        i += 1


z = zakres2(10)  # obiekt generatora
# for i in z:
#     print(i)

while True:
    try:
        print(next(z))
    except StopIteration:
        break


def fib2(n=inf):
    a, b = 1, 1
    while a < n:
        yield a
        a, b = b, a + b


f = fib2()

# while True:
#     try:
#         print(next(f))
#     except StopIteration:
#         break
for i in fib2():
    if i > 100:
        break
    print(i)
