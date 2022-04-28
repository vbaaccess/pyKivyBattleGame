import time
import asyncio
import websockets


class Server:

    clients = {}            # dziennik klientow
    games = {}              # dziennik gier
    websocketToGame = {}    # weboscke, ID Gry

    def __init__(self):
        self.clients = {}

    async def echo(self, websocket, path):
        try:
            async for message in websocket:
                # testowe spowolnienie wyswietlania otrzymywanych komunikatow
                await asyncio.sleep(1)

                # dodanie nowego wpisu jesli nie istnieje
                if websocket not in self.clients:
                    self.clients[websocket] = True

                # wpis: otrzymalem wiadomosc
                for client_ws in self.clients:
                    if client_ws == websocket:
                        print(f'Otrzymano wiadomosc:', message)

                # wyslanie wiadomosci do wszystkich klientow z wylaczeniem nadawcy
                # wpis: rozsylam otrzymana wiadomosc do pozostalych
                #   klucz
                if len(self.clients) > 1:
                    print('Forwarding the message:')

                # for client_ws in self.clients:
                #     if client_ws == websocket:
                #         continue
                #     print(f' to {client_ws}: ', message)
                #     await client_ws.send(message)
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
