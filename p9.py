import asyncio
from time import sleep

async def say_after(what, when):
    await asyncio.sleep(when)
    return what

async def hello(x, name):  # funkcja bez return, ale zwraca koprocedurę
    try:
        print(await say_after(f"{name}: Witaj!...", 0))
        print(await say_after(f"{name}: Żegnaj!...", x))
        if name.split(" ")[0] != f"koniec":
            asyncio.get_event_loop().create_task(hello(x, f"koniec {name}"))
    except asyncio.CancelledError:
        print(f"{name}: Kończę zadanie po żądaniu anulowania")


def blocking():
    print('Tu początek procedury blokującej!')
    sleep(3)
    print('Tu koniec procedury blokującej!')

""" # niskopoziomowa implementacja
# print(type(hello('1', .1))) # coroutine
# print(type(hello(2., '1'))) 
# print(dir(hello(2., '1'))) # await, send, throw
coro1 = hello(2., '1')
coro2 = hello(1., '2')

loop = asyncio.get_event_loop()

task1 = loop.create_task(coro1)
task2 = loop.create_task(coro2)

grupa = asyncio.gather(task1, task2)

loop.run_until_complete(grupa)
pending = asyncio.all_tasks(loop = loop)
for task in pending:  # jeśli nie chcemy zakańczać to komentujemy te linie
    task.cancel()     # cancel to wstrzyknięcie wyjątku
grupa = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(grupa)

loop.close()
"""

async def main():
    coro1 = hello(2., '1')
    coro2 = hello(1., '2')
    # grupa = asyncio.gather(coro1, coro2, blocking()) # gdy na siłę async
    grupa = asyncio.gather(coro1, coro2, asyncio.get_event_loop().run_in_executor(None, blocking))
    await grupa
    # Żeby nie kończyć zadań potomnych
    pending = asyncio.all_tasks(loop = asyncio.get_event_loop())
    pending = (t for t in pending if t is not asyncio.current_task())
    grupa = asyncio.gather(*pending, return_exceptions=True)
    await grupa
    

asyncio.run(main())
