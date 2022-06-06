
def zapisz(sciezka):
    f = open(sciezka, 'w')
    while True:
        try:
            x = yield
            f.write(x)
        except GeneratorExit:
            f.close()
            print('teraz działa metoda close')
            break


z = zapisz('1.txt')
z.send(None)
z.send('a')
z.send('b')

# z=2

print('Koniec')

##################


def suma(s=0):
    while True:
        try:
            x = yield s
            s += float(x)
        except GeneratorExit:  # albo yield poza try
            break
        except:
            pass


su = suma()
su.send(None)
print(su.send(1))
print(su.send(2))
print(su.send(3))
print(next(su))

#####################


class MójWyjątek(BaseException):  # Exception
    pass

#raise MójWyjątek


su.throw(MójWyjątek)  # nic się nie dzieje, bo except: pass
# z.throw(MójWyjątek)

###################


class WyjątekZerujący(BaseException):
    pass


def suma(s=0.):
    while True:
        try:
            x = yield s
            s += float(x)
        except GeneratorExit:  # albo yield poza try
            break
        except WyjątekZerujący:
            s = 0.
        except:
            pass


su = suma()
su.send(None)
print(su.send(1))
print(su.send(2))
print(su.send(3))
su.throw(WyjątekZerujący)
print(next(su))

print('#'*40)
###############


class InException(BaseException):
    pass


class OutException(BaseException):
    pass


def suma(s=0.):
    global wynik
    while True:
        try:
            yield
        except GeneratorExit:  # albo yield poza try
            break
        except WyjątekZerujący:
            s = 0.
        except InException as e:
            s += e.args[0]
        except OutException:
            wynik = OutException(s)
        # except:
        #	pass


su = suma()
su.send(None)
su.throw(InException(1))
su.throw(InException(3))
su.throw(OutException)
print(wynik.args[0])
su.throw(InException(5))
su.throw(OutException)
print(wynik.args[0])
