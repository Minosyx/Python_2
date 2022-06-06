import asyncio


async def polaczenie(reader, writer):
    print('Połączono')
    while True:
        data = await reader.read(1024)
        print(f"Odebrano: {data.decode()}")
        if not data:
            writer.close()
            await writer.wait_closed()
            print('Rozłączono')
            break
        writer.write(data)
        await writer.drain()
        print(f'Wysłano: {data.decode()}')


async def main():
    server = await asyncio.start_server(polaczenie, host='localhost', port=4444)
    # try:
    #     await server.serve_forever()
    # except:
    #     server.close()
    #     await server.wait_closed()
    async with server:
        await server.serve_forever()
    print('Zamykamy')

asyncio.run(main())
