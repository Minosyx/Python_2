
from functools import reduce  # w pythonie 2 jeszcze funkcja wbudowana
import itertools as it
l = [i**2 for i in range(10)]  # lista składana
print(l)

for i in l:
    print(i)

l = (i**2 for i in range(10))  # wyrażenie generatora
print(l)
print(dir(l))

for i in l:
    print(i)


def ll():
    for i in range(10):
        yield(i**2)


print(dir(ll()))

for i in ll():
    print(i)

l = map(lambda i: i**2, range(10))
print(l)
print(dir(l))

for i in l:
    print(i)


print(dir(it))

# aż się wyczerpie najkrótszy argument
z = zip(('a', 'b', 'c'), (1, 2, 3), 3*['X'], 'KOTY')
print(dir(z))
print(list(z))

# w pythonie 2: imap, ifilter, izip

# aż się wyczerpie najkrótszy argument
z = it.zip_longest(('a', 'b', 'c'), (1, 2, 3), 3*['X'], 'KOTY', fillvalue='')
print(dir(z))
print(list(z))

for i in it.repeat('a', 10):
    print(i)

# for i in it.cycle('abc'):
#	print(i)

for i in it.count(5, 5):
    print(i)
    if i > 100:
        break

for i in it.accumulate(range(10)):
    print(i)

print(it.accumulate.__doc__)

for i in it.accumulate(range(1, 10), int.__mul__):
    print(i)


print(reduce(int.__add__, range(1, 10)))  # = 1+2+3+...+9 = 45

i1 = range(1, 10)
i2 = range(2, 11)

iloczyny = (i*j for i, j in zip(i1, i2))

for i in iloczyny:
    print(i)

iloczyny = it.starmap(int.__mul__, zip(i1, i2))

for i in iloczyny:
    print(i)

i = iter(range(10))

for j in it.islice(i, 1, 6, 2):  # 1, 3, 5
    print(j)

for j in i:						# 6,7,8,9
    print(j)

for j in i:						# nic
    print(j)

# czy ostatnia cyfra lizby mniejsza niż 5	różnica z filter!
for i in it.takewhile(lambda i: (i % 10) < 5, range(20)):
    print(i)

print('#'*10)

# czy ostatnia cyfra lizby mniejsza niż 5	różnica z filter!
for i in it.dropwhile(lambda i: (i % 10) < 5, range(20)):
    print(i)

# czy ostatnia cyfra lizby mniejsza niż 5	różnica z filter!
for i in it.filterfalse(lambda i: (i % 10) < 5, range(20)):
    print(i)

##############
print('#'*40)

n = 3
i = iter(range(10))

for i in zip(*n*[i]):
    print(i)

i = iter(range(10))

for i in zip(*it.tee(i, n)):
    print(i)

###############

print('#'*40)
for i in it.permutations('abc'):
    print(i)

print('#'*40)
for i in it.product(*2*['abc']):
    print(i)

print('#'*40)
for i in it.combinations('abc', 2):
    print(i)

print('#'*40)
for i in it.combinations_with_replacement('abc', 2):
    print(i)

###############

i1 = 'ABCD'
i2 = 'abcd'

# iterator po wszystkich ciągach 8-elementowych elementów z i1 i i2, takich że każdy element dokładnie raz i kolejności pomiędzy elementami i1 oraz pomiędzy elementami i2 są zachowane: np AabBCDcd


def nowy():
    for i in it.combinations(range(8), 4):
        it1 = iter(i1)
        it2 = iter(i2)
        yield [next(it1 if j in i else it2) for j in range(8)]


for i in nowy():
    print(i)
