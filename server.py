from socket import socket, SOL_SOCKET, SO_REUSEADDR
from Mikrowatki import Mikrowatek, Zarzadca, ReadWait, WriteWait, New

s = socket()
s.bind(('localhost', 4444))
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.listen(1)


def nowe_polaczenia(s):
    print(s)
    while True:
        yield ReadWait(s)
        m = Mikrowatek(polaczenie(s.accept()[0]))
        yield New(m)


def polaczenie(c):
    print(c)
    while True:
        yield ReadWait(c)
        x = c.recv(1024)
        if x == '':
            c.close()
            break
        yield WriteWait(c)
        c.sendall(x)


z = Zarzadca()
m = Mikrowatek(nowe_polaczenia(s)).start(z)
z.run()

