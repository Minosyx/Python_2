import itertools as it
from copy import deepcopy

# i1 = 'ABCD'
# i2 = 'abcd'


# def ciag():
#     c = iter(i1 + i2)
#     for i in it.permutations(c):
#         yield([*i])

# def ciag():
#     for i in it.permutations(range(8)):
#         c = i1 + i2
#         yield([c[x] for x in i])


# for i in ciag():
#     print(i)

# zadanie 1

# words = ['xd', '23', ',.?']
# lw = list(map(len, words))


# def shuffle(strings):
#     return list({''.join(l.pop(0) for l in deepcopy(p)) for p in it.permutations(it.chain.from_iterable(it.repeat(list(s), len(s)) for s in strings))})


# def shuffleN(strings):
#     a = (it.chain.from_iterable(it.repeat(list(s), len(s)) for s in strings))
#     k = []
#     for p in it.permutations(a):
#         k.append(''.join(l.pop(0) for l in deepcopy(p)))
#     return set(k)


# c = shuffleN(words)
# print(c)
# print(len(c))

# def fill(nonel, val, amount):
#     pos = [i for i in range(len(nonel)) if nonel[i] is None]
#     return ([val if i in k else nonel[i] for i in range(len(nonel))] for k in it.combinations(pos, amount))


# nones = [[None]*sum(lw)]
# for j in range(len(lw)):
#     nones = it.chain(*(fill(i, j, lw[j]) for i in nones))


# def f(indexes):
#     its = list(map(iter, words))
#     return ''.join([next(its[indexes[j]]) for j in range(sum(lw))])


# iterator = (f(i) for i in nones)

# print([i for i in iterator])

# zadanie 2

# def dict(x, y):
#     for i in it.product(*it.tee(y, len(x))):
#         b = iter(i)
#         yield({a: next(b) for a in x})


# x = ('X', 'Y', 'Z')
# y = range(5)

# for i in dict(x, y):
#     print(i)

# zadanie 3

# def dict1(x, y):
#     for i in it.permutations(y, len(x)):
#         b = iter(i)
#         yield({a: next(b) for a in x})


# x = ('X', 'Y', 'Z')
# y = range(4)

# for i in dict1(x, y):
#     print(i)

# zadanie 4

# def dict2(x, y):  #zakomentowane malejace
#     # x = x[::-1]
#     for i in it.combinations(y, len(x)):
#         b = iter(i)
#         yield({a: next(b) for a in x})


# x = ('X', 'Y', 'Z')
# y = range(5)

# for i in dict2(x, y):
#     # i = sorted(i.items(), key= lambda x: x[0])
#     print(i)

# zadanie 5

def dict3(x, y):
    # x = x[::-1] #zaklomentowane nierosnace
    for i in it.combinations_with_replacement(y, len(x)):
        b = iter(i)
        yield({a: next(b) for a in x})


x = ('X', 'Y', 'Z')
y = range(5)

for i in dict3(x, y):
    # i = sorted(i.items(), key=lambda x:x[0])
    # i = dict(i)
    print(i)
