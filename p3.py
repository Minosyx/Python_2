
def konsument():
    while True:
        x = yield 'Hello'
        print('From konsument: ', x)


print(konsument)
k = konsument()
print(k)
# print(dir(k))

k.send(None) # <- inicjalizacja
for i in range(5):
    print('Konsument returns: ', k.send(i))


next(k) # k.send(None)

###################


def stos(l):
    s = None
    while True:
        x = yield s
        if x is None:
            try:
                s = l.pop() 
            except:
                raise StopIteration from None
        else:
            s = None
            l.append(x)


s = stos([1, 2, 3])
# stan stosu: 1, 2, 3
s.send(None)
print(next(s))
print(next(s))
print(next(s))
s.send('a')
print(next(s))
s.send(5)
print(next(s))
print(next(s))
