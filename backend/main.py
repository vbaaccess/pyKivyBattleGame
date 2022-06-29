import time
import math
import asyncio
import websockets
from backend.game import Game


class Server:
    clearInterval = 60  # czestotliwosc czyzcenia (delete) gier
    games = {}  # dziennik gier: Id obiektu gry
    websocketToGame = {}  # weboscke, ID Gry

    gameKeys = ['A', 'B', 'C']

    def __init__(self):
        print('Constructor')

    async def clearOldGames(self):
        while True:
            size = len(self.games)
            if size == 0:
                print("No game to clear")
                await asyncio.sleep(self.clearInterval)
                continue
            print("Starting cleanup")
            for key in self.games.copy():
                if time.time() - self.games[key].lastActivity > self.clearInterval:
                    try:
                        await self.games[key].timeout()
                    except:
                        print("Error during timeout notification")
                    print("Game deleted", key)
                    del self.games[key]
                await asyncio.sleep(self.clearInterval / size)

    async def echo(self, websocket, path):
        try:
            async for message in websocket:
                # testowe spowolnienie wyswietlania otrzymywanych komunikatow
                await asyncio.sleep(1)

                # dodwanie nowego gracza
                if websocket not in self.websocketToGame:
                    pom = math.floor(len(self.websocketToGame) / 2)
                    self.websocketToGame[websocket] = self.gameKeys[pom]
                    if self.websocketToGame[websocket] in self.games:
                        game_ws = self.websocketToGame[websocket]
                        print("Adding player to game", game_ws)
                        self.games[game_ws].add_player(websocket)  # STEP 1/1 dodaje gracza do gry
                    else:
                        game_ws = self.websocketToGame[websocket]
                        print("Creating game and add player", game_ws)
                        self.games[game_ws] = Game()  # STEP 1/2 tworze gre
                        self.games[game_ws].add_player(websocket)  # STEP 2/2 dodaje gracza do gry

                # tworzenie gry (jesli istnieje)
                game_ws = self.websocketToGame[websocket]

                if game_ws in self.games:
                    game = self.games[game_ws]
                    await game.handle(websocket, message)

        except websockets.exceptions.ConnectionClosed:
            game_ws = self.websocketToGame[websocket]

            if game_ws in self.games:
                game = self.games[game_ws]
                try:
                    await game.handleDisconnect(websocket)
                except Exception as e:
                    print(f'Server.echo Error. {e.__doc__}: {e.message}')
            self.websocketToGame.pop(websocket)
        except RuntimeError as e:
            print(f'Server.echo Error. {e.__doc__}: {e.message}')


if __name__ == '__main__':
    print('Start server')
    s = Server()
    server_name = 'localhost'
    server_port = 8765
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(s.echo, server_name, server_port)
    )

    asyncio.get_event_loop().run_until_complete(
        s.clearOldGames()
    )

    asyncio.get_event_loop().run_forever()
