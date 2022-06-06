from socket import socket, SOL_SOCKET, SO_REUSEADDR
from select import select

s = socket()
s.bind(('localhost', 4444))
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.listen(1)

c1, *_ = s.accept()
c2, *_ = s.accept()

r_wait = [c1, c2]
w_wait = {}

while r_wait or w_wait:
    r_ready, w_ready, e = select(r_wait, w_wait.keys(), [], .1)
    for c in r_ready:
        x = c.recv(1024)
        if x:
            w_wait[c] = x
        else:
            c.close()
        r_wait.remove(c)
    for c in w_ready:
        c.sendall(w_wait.pop(c))
        r_wait.append(c)

s.close()
