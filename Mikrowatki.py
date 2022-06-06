from select import select
import queue

class Mikrowatek:
    def __init__(self, target):
        self.target = target

    def run(self):
        return self.target.send(None)

    def start(self, zarzadca):
        zarzadca.task(self)


class SystemCall:
    def __call__(self, mikrowatek, zarzadca):
        raise NotImplementedError


class Zarzadca:
    def __init__(self):
        self.kolejka = queue.Queue()
        self.RWAIT = {}
        self.WWAIT = {}
        self.task(Mikrowatek(target=system()))

    def task(self, t):
        self.kolejka.put(t)

    def run(self):
        poprzednie = None
        while True:
            t = self.kolejka.get()
            if poprzednie and t == poprzednie:
                break
            if not (t in self.RWAIT.values() or t in self.WWAIT.values()):
                try:
                    sc = t.run()
                    if isinstance(sc, SystemCall):
                        sc(t, self)
                    self.kolejka.put(t)
                except StopIteration:
                    pass
            else:
                self.kolejka.put(t)
            poprzednie = t


class ReadWait(SystemCall):
    def __init__(self, obiekt):
        self.obiekt = obiekt

    def __call__(self, mikrowatek, zarzadca):
        zarzadca.RWAIT[self.obiekt] = mikrowatek


class WriteWait(SystemCall):
    def __init__(self, obiekt):
        self.obiekt = obiekt

    def __call__(self, mikrowatek, zarzadca):
        zarzadca.WWAIT[self.obiekt] = mikrowatek


class New:
    def __init__(self, mikrowatek):
        self.z = Zarzadca()
        self.mikrowatek = mikrowatek
        self.start()

    def start(self):
        self.mikrowatek.start(self.z)
        self.z.run()


class System(SystemCall):
    def __call__(self, mikrowatek, zarzadca):
        print(zarzadca.RWAIT, zarzadca.WWAIT)
        Rready, Wready = select(zarzadca.RWAIT.keys(),
                                zarzadca.WWAIT.keys(), [], .1)[:2]
        for i in Rready:
            zarzadca.RWAIT.pop(i)
        for i in Wready:
            zarzadca.WWAIT.pop(i)


def system():
    while True:
        yield System()
