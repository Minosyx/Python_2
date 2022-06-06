import asyncio

class Feed:     # asynchroniczny iterator
    def __init__(self, reader):
        self.reader = reader
    
    __aiter__ = lambda self: self

    async def __anext__(self):
        data = await self.reader.read(1024)
        if data:
            return data
        raise StopIteration


async def Feed_g(reader):       # asynchroniczna funkcja generatora
    while True:
        data = await reader.read(1024)
        if not data:
            break
        yield data


async def polaczenie(reader, writer):
    print('Połączono')
    # async for line in Feed(reader):
    # async for line in Feed_g(reader):
    #     print(line.decode())
    # it = (line.decode() async for line in Feed(reader))       # asynchroniczne wyrażenie generatora
    # async for i in it:
    #     print(i)
    lista = [line.decode() async for line in Feed_g(reader)]
    print(lista)        # asynchroniczne wyrażenie listy składanej
    print('Rozłączono')


async def main():
    server = await asyncio.start_server(polaczenie, host='localhost', port=4444)
    async with server:
        await server.serve_forever()
    print('Zamykamy')

asyncio.run(main())
