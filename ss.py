from socket import socket, SOL_SOCKET, SO_REUSEADDR
from select import select
from queue import Queue


class Mikrowatek:

    def __init__(self, target):
        self.target = target

    def run(self):
        return self.target.send(None)

    def start(self, zarzadca):
        zarzadca.nowe_zadanie(self)


class Zarzadca:

    def __init__(self):
        self.kolejka_zadan = Queue()
        self.Wwait = {}
        self.Rwait = {}
        self.nowe_zadanie(Mikrowatek(target=release()))

    def nowe_zadanie(self, zadanie):
        self.kolejka_zadan.put(zadanie)

    def run(self):
        poprzednie = None
        while True:
            zadanie = self.kolejka_zadan.get()
            if poprzednie and zadanie == poprzednie:
                break
            if not (zadanie in self.Rwait.values() or zadanie in self.Wwait.values()):
                try:
                    sc = zadanie.run()
                    if isinstance(sc, SystemCall):
                        sc(zadanie, self)
                    self.kolejka_zadan.put(zadanie)
                except StopIteration:
                    pass
            else:
                self.kolejka_zadan.put(zadanie)
            poprzednie = zadanie


class SystemCall:

    def handle(self, mikrowatek, zarzadca):
        raise NotImplementedError


class ReadWait(SystemCall):

    def __init__(self, obiekt):
        self.obiekt = obiekt

    def __call__(self, mikrowatek, zarzadca):
        zarzadca.Rwait[self.obiekt] = mikrowatek


class WriteWait(SystemCall):

    def __init__(self, obiekt):
        self.obiekt = obiekt

    def __call__(self, mikrowatek, zarzadca):
        zarzadca.Wwait[self.obiekt] = mikrowatek


class Release(SystemCall):

    def __call__(self, mikrowatek, zarzadca):
        print(zarzadca.Rwait, zarzadca.Wwait)
        Rready, Wready = select(zarzadca.Rwait.keys(),
                                zarzadca.Wwait.keys(), [], .1)[:2]
        for i in Rready:
            zarzadca.Rwait.pop(i)
        for i in Wready:
            zarzadca.Wwait.pop(i)


def release():
    while True:
        yield Release()


###########################


s = socket()
s.bind(('localhost', 4445))
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.listen(1)


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
m1 = Mikrowatek(polaczenie(s.accept()[0])).start(z)
m2 = Mikrowatek(polaczenie(s.accept()[0])).start(z)
z.run()
