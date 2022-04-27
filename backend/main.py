import time
import asyncio
import websockets


class Server:

    clients = {}    # dziennik klientow

    def __init__(self):
        self.clients = {}

    async def echo(self, websocket, path):
        try:
            async for message in websocket:
                # dodanie nowego wpisu jesli nie istnieje
                if websocket not in self.clients:
                    self.clients[websocket] = True

                # wyslanie wiadomosci do wszystkich klientow z wylaczeniem nadawcy
                #   klucz
                for client_ws in self.clients:
                    if client_ws == websocket:
                        continue
                    # print('Server msg:', message)
                    await client_ws.send(message)
        except RuntimeError:
            print('Server.echo Error')


if __name__ == '__main__':
    print('Start server')
    s = Server()
    server_name = 'localhost'
    server_port = 8765
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(s.echo, server_name, server_port)
    )
    asyncio.get_event_loop().run_forever()
