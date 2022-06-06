
def konsument():
    while True:
        x = yield 'Hello'
        print('From konsument: ', x)


print(konsument)
k = konsument()
print(k)
print(dir(k))

k.send(None)									# <- inicjalizacja
for i in range(5):
    print('Konsument returns: ', k.send(i))
print('Konsument returns: ', next(k))			# k.send(None)

############


def stos(l):
    s = None
    while True:
        x = yield s
        if x == None:
            try:
                s = l.pop()
            except:
                raise StopIteration from None
        else:
            l.append(x)
            s = None


s = stos([1, 2, 3])
s.send(None)
# stan stosu: 1,2,3
print(next(s))		# 3
# stan stosu: 1,2
s.send('a')
# stan stosu: 1,2,'a'
print(next(s))		# 'a'
# stan stosu: 1,2
while True:
    print(next(s))
