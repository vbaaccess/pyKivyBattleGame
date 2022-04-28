import time
import math
import asyncio
import websockets
from backend.game import Game

class Server:

    clients = {}            # dziennik klientow
    games = {}              # dziennik gier
    websocketToGame = {}    # weboscke, ID Gry

    gameKeys = ['A', 'B', 'C']

    def __init__(self):
        self.clients = {}

    async def echo(self, websocket, path):
        try:
            async for message in websocket:
                # testowe spowolnienie wyswietlania otrzymywanych komunikatow
                await asyncio.sleep(1)

                # dodwanie nowego gracza
                if websocket not in self.websocketToGame:
                    pom = math.floor(len(self.websocketToGame) /2)
                    self.websocketToGame[websocket] = self.gameKeys[pom]
                    if self.websocketToGame[websocket] in self.games:
                        game_ws = self.websocketToGame[websocket]
                        print("Adding player to game", game_ws)
                        self.games[game_ws].add_player(websocket)               # STEP 1/1 dodaje gracza do gry
                    else:
                        game_ws = self.websocketToGame[websocket]
                        print("Creating game and add player", game_ws)
                        self.games[game_ws] = Game()                            # STEP 1/2 tworze gre
                        self.games[game_ws].add_player(websocket)               # STEP 2/2 dodaje gracza do gry

                # tworzenie gry
                game_ws = self.websocketToGame[websocket]
                game = self.games[game_ws]
                if len(game.players) == 2:
                    await game.handle(websocket, message)

                # if websocket is self.websocketToGame:
                #     game = self.websocketToGame[websocket]
                #     if len(game.players) == 2:
                #         await game.handle(websocket, message)
                # else:
                #     self.websocketToGame[websocket] = self.gameKeys[round(len(self.websocketToGame) / 2)]
                #     if self.websocketToGame[websocket] in self.games:
                #         self.games[self.websocketToGame[websocket]].add_player(websocket)
                #     else:
                #         self.games[self.websocketToGame[websocket]] = Game()
                #         self.games[self.websocketToGame[websocket]].add_player(websocket)


                # # dodanie nowego wpisu jesli nie istnieje
                # if websocket not in self.clients:
                #     self.clients[websocket] = True

                # # wyslanie wiadomosci do wszystkich klientow z wylaczeniem nadawcy
                # # wpis: rozsylam otrzymana wiadomosc do pozostalych
                # #   klucz
                # if len(self.clients) > 1:
                #     print('Forwarding the message:')

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
