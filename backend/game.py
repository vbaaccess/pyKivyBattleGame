import time


class Game:
    lastActivity = time.time()
    players = []

    def __init__(self):
        self.players = []
        self.lastActivity = time.time()

    def add_player(self, websocket):
        self.players.append(websocket)

    async def handle(self, websocket, message):
        if len(self.players) == 2:
            self.sendToOther(websocket, message)

    async def sendToOther(self, websocket, message):
        # wyslanie wiadomosci do wszystkich klientow z wylaczeniem nadawcy
        # wpis: rozsylam otrzymana wiadomosc do pozostalych
        #   klucz
        if len(self.player) > 1:
            print('Forwarding the message:')

        # player = > client websocket
        for player in self.players:
            if player == websocket:
                continue
            print(f' to {player}: ', message)
            await player.send(message)

    async def timeout(self):
        # send message to all players
        for player in self.players:
            await player.send("Timeout")

    async def handleDisconnect(self, websocket):
        if self.players == 1:
            return
        await self.sendToOther(websocket, "Opponent Disconnect")
        if self.players[0] == websocket:
            del self.players[0]
        else:
            del self.players[1]
