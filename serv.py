import asyncio

d = {}


def validate(data):
    if data == b'':
        return ">Nie może być pusty, podaj swój nick: ".encode("utf8")
    elif data in d:
        return ">Już w słowniku, podaj swój nick: ".encode("utf8")
    elif b'*' in data or b'<' in data or b'>' in data:
        return ">Podano niedozwolony znak w nicku. Podaj nowy nick: ".encode("utf8")


async def con(reader, writer):
    writer.write(">Witamy na serwerze, podaj swój nick: ".encode("utf8"))
    await writer.drain()
    data = await reader.readuntil(b'\n')
    while True:
        if data == b'':
            writer.close()
            return
        data = data.strip()
        v = validate(data)
        if v is None:
            d[data] = writer
            nick = data
            break
        writer.write(v)
        await writer.drain()
        data = await reader.readuntil(b'\n')
    writer.write(">Teraz możesz wysyłać i odbierać wiadomości\n".encode("utf8"))
    await writer.drain()
    while True:
        data = await reader.readuntil(b'\n')
        if data == b'':
            writer.close()
            return
        data = data.strip()
        if b'<' not in data:
            writer.write(">Nieprawidłowy format wiadomości\n".encode("utf8"))
            await writer.drain()
            continue
        adr, message = data.split(b'<', 1)
        ca = d.get(adr)
        if adr == b'*':
            for x in d:
                if x != nick:
                    d[x].write(nick + b'>' + message + b'\n')
                    await d[x].drain()
        elif b',' in adr:
            for a in adr.split(b','):
                if a != nick and a in d:
                    d[a].write(nick + b'>' + message + b'\n')
                    await d[a].drain()
        elif ca is None and message == b"E":
            break
        elif ca is None and message == b"L":
            writer.write(">Dostępni użytkownicy:\n".encode("utf8"))
            await writer.drain()
            for x in d:
                if x != nick:
                    writer.write(x + b'\n')
                    await writer.drain()
        elif ca is None:
            writer.write(">Użytkownik nie istnieje\n".encode("utf8"))
            await writer.drain()
            continue
        else:
            ca.write(nick + b'>' + message + b'\n')
            await ca.drain()
    del d[nick]
    writer.close()


async def main():
    server = await asyncio.start_server(con, 'localhost', 4444)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
