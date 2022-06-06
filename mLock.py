
from time import sleep
from threading import Thread


class MLock:
    def __init__(self):
        self.b = False

    def __enter__(self):
        while self.b:
            pass
        self.b = True

    def __exit__(*args):
        args[0].b = False


def f(x):
    # with b:
        for i in range(5):
            with b:
                print(x, i)
            sleep(1e-5)


b = MLock()
Thread(target=f, args=('A',)).start()
Thread(target=f, args=('B',)).start()
