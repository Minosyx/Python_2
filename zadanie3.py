from socket import socket, SOL_SOCKET, SO_REUSEADDR
from threading import Thread


def polaczenie(c, a):
    print('Połączenie z adresu %s' % (a,))
    while True:
        x = c.recv(1024)
        if x == b'':
            c.close()
            break
        c.sendall(x)
    print('Połączenie z adresu %s zakończone' % (a,))


s = socket()
s.bind(('localhost', 4444))
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.listen(1)
try:
    while True:
        w = Thread(target=polaczenie, args=s.accept())
        w.daemon = True
        w.start()
finally:
    s.close()
